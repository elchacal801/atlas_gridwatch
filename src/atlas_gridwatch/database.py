import json
import logging
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
from .models import DataCenter

logger = logging.getLogger(__name__)

class InfrastructureDatabase:
    """
    Manages persistence of infrastructure assets (Data Centers, Cables)
    to a JSON master file, handling deduplication and merging.
    """

    def __init__(self, db_path: Path = Path("data/processed/infrastructure_master.json")):
        self.db_path = db_path
        self.data: Dict[str, Dict] = {} # Keyed by ID
        self._load()

    def _load(self):
        """Loads existing data from JSON."""
        if not self.db_path.exists():
            self.data = {}
            return
        
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                raw_list = json.load(f)
                # Convert list back to dict keyed by ID for O(1) access
                for item in raw_list:
                    # Robustness: Handle if item is missing 'id'
                    oid = item.get('id')
                    if oid:
                        self.data[oid] = item
        except Exception as e:
            logger.error(f"Failed to load DB: {e}")
            self.data = {}

    def save(self):
        """Persists data to JSON."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.db_path, 'w', encoding='utf-8') as f:
            # Sort by name for clean diffs
            sorted_list = sorted(list(self.data.values()), key=lambda x: x.get('name', ''))
            json.dump(sorted_list, f, indent=2)

    def upsert_asset(self, asset: DataCenter):
        """
        Inserts or Updates an asset. 
        Simple merge strategy: New overwrites old.
        """
        # Convert model to dict
        asset_dict = asset.model_dump(mode='json')
        self.data[asset.id] = asset_dict
        
    def bulk_upsert(self, assets: List[DataCenter]):
        for a in assets:
            self.upsert_asset(a)
        self.save()

    def get_all(self) -> List[Dict]:
        return list(self.data.values())


class NewsDatabase:
    """
    Manages a local SQLite database for archiving processed RSS news items.
    Enables historical retrieval and basic keyword search for RAG.
    """
    
    def __init__(self, db_path: str = "data/news_archive.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        """Initialize the database schema and FTS tables."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS articles (
                        url TEXT PRIMARY KEY,
                        title TEXT,
                        source TEXT,
                        published_date TEXT,
                        summary TEXT,
                        risk_score TEXT,
                        content TEXT,
                        embedding BLOB,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                # Attempt to enable Full Text Search (FTS5)
                try:
                    conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS articles_fts USING fts5(title, summary, content='articles', content_rowid='rowid')")
                    conn.execute("""
                        CREATE TRIGGER IF NOT EXISTS articles_ai AFTER INSERT ON articles 
                        BEGIN 
                            INSERT INTO articles_fts(rowid, title, summary) VALUES (new.rowid, new.title, new.summary); 
                        END
                    """)
                except sqlite3.OperationalError:
                    logger.warning("SQLite FTS5 not available. Falling back to basic LIKE search.")

        except Exception as e:
            logger.error(f"Database initialization failed: {e}")

    def upsert_article(self, article: Dict[str, Any]):
        """
        Insert or Update an article. Uses URL as the unique key.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT INTO articles (url, title, source, published_date, summary, risk_score)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(url) DO UPDATE SET
                        title=excluded.title,
                        summary=excluded.summary,
                        risk_score=excluded.risk_score
                """, (
                    article.get("url"),
                    article.get("title"),
                    article.get("source"),
                    article.get("published_date", ""),
                    article.get("summary", ""),
                    article.get("risk", "UNKNOWN")
                ))
        except Exception as e:
            logger.error(f"Failed to upsert article {article.get('url')}: {e}")

    def search_articles(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search articles by keyword using FTS if available, or LIKE.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            
            # 1. Try FTS Search
            try:
                cursor = conn.execute("""
                    SELECT * FROM articles 
                    WHERE rowid IN (SELECT rowid FROM articles_fts WHERE articles_fts MATCH ? ORDER BY rank)
                    LIMIT ?
                """, (f'"{query}"', limit))
                return [dict(row) for row in cursor.fetchall()]
            except:
                # 2. Fallback to LIKE
                cursor = conn.execute("""
                    SELECT * FROM articles 
                    WHERE title LIKE ? OR summary LIKE ?
                    ORDER BY published_date DESC
                    LIMIT ?
                """, (f"%{query}%", f"%{query}%", limit))
                return [dict(row) for row in cursor.fetchall()]

    def get_context_for_analysis(self, keywords: List[str], limit_per_keyword: int = 3) -> str:
        """
        Retrieves a consolidated text context for LLM analysis based on a list of keywords.
        """
        seen_urls = set()
        context_lines = []
        
        for kw in keywords:
            results = self.search_articles(kw, limit_per_keyword)
            for res in results:
                if res['url'] not in seen_urls:
                    context_lines.append(f"- [{res['published_date']}] {res['title']} ({res['source']}): {res['summary']}")
                    seen_urls.add(res['url'])
        
        return "\\n".join(context_lines) if context_lines else "No relevant news found in local archive."
