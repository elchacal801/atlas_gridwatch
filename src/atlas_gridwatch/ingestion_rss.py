import feedparser
import logging
from typing import List, Dict, Any
from datetime import datetime
from .ingestion import BaseIngestor
from .database import NewsDatabase

logger = logging.getLogger(__name__)

class RSSIngestor(BaseIngestor):
    """
    Ingests OSINT from industry RSS feeds.
    """
    
    FEEDS = [
        # Tech & Infrastructure
        {"url": "https://www.datacenterdynamics.com/en/rss/", "category": "Tech & Infrastructure"},
        {"url": "https://datacenterfrontier.com/feed/", "category": "Tech & Infrastructure"},
        {"url": "https://www.nextgov.com/rss/all/", "category": "Tech & Infrastructure"},
        {"url": "https://www.theregister.com/headlines.atom", "category": "Tech & Infrastructure"},
        {"url": "https://datacenterpost.com/feed/", "category": "Tech & Infrastructure"},
        {"url": "https://blogs.cisco.com/datacenter/feed", "category": "Tech & Infrastructure"},
        {"url": "https://www.serverfarmllc.com/feed/", "category": "Tech & Infrastructure"},

        # Maritime & Cables
        {"url": "https://subtelforum.com/feed/", "category": "Maritime & Cables"},
        {"url": "https://www.navalnews.com/feed/", "category": "Maritime & Cables"},
        {"url": "https://maritime-executive.com/articles.rss", "category": "Maritime & Cables"},
        {"url": "https://news.usni.org/feed", "category": "Maritime & Cables"},

        # Defense & Security
        {"url": "https://www.defenseone.com/rss/all/", "category": "Defense & Security"},
        {"url": "https://www.c4isrnet.com/arc/outboundfeeds/rss/", "category": "Defense & Security"},
        {"url": "https://www.csis.org/rss.xml", "category": "Defense & Security"},
        {"url": "https://breakingdefense.com/feed/", "category": "Defense & Security"},
        
        # Geopolitics
        {"url": "https://warontherocks.com/feed/", "category": "Geopolitics"},
        {"url": "https://thediplomat.com/feed/", "category": "Geopolitics"},
        {"url": "https://foreignpolicy.com/feed", "category": "Geopolitics"},
        {"url": "https://www.aspistrategist.org.au/feed/", "category": "Geopolitics"},
        {"url": "https://www.lawfareblog.com/rss.xml", "category": "Geopolitics"},
        {"url": "https://geostrategy-direct.com/feed/", "category": "Geopolitics"},
        {"url": "https://www.thecipherbrief.com/feeds/feed.rss", "category": "Geopolitics"},
        {"url": "https://geopoliticalmatters.com/feed/", "category": "Geopolitics"},
        {"url": "https://www.foreignaffairs.com/feeds/topic/Geopolitics/rss.xml", "category": "Geopolitics"},
        {"url": "https://www.ft.com/geopolitics?format=rss", "category": "Geopolitics"},

        # Cyber & Intelligence
        {"url": "https://www.bellingcat.com/feed/", "category": "Cyber & Intel"},
        {"url": "https://therecord.media/feed/", "category": "Cyber & Intel"},
        {"url": "https://krebsonsecurity.com/feed/", "category": "Cyber & Intel"},
        {"url": "https://thecyberwire.com/feeds/rss.xml", "category": "Cyber & Intel"},
        {"url": "https://www.bleepingcomputer.com/feed/", "category": "Cyber & Intel"},
        {"url": "https://www.darkreading.com/rss.xml", "category": "Cyber & Intel"},
        {"url": "https://feeds.feedburner.com/TheHackersNews?format=xml", "category": "Cyber & Intel"},

        # Quantum Tech
        {"url": "https://quantumcomputingreport.com/feed/", "category": "Quantum Tech"},
        {"url": "https://quantum-journal.org/feed/", "category": "Quantum Tech"},
        {"url": "https://www.insidequantumtechnology.com/feed/", "category": "Quantum Tech"},
        {"url": "https://quantumzeitgeist.com/feed/", "category": "Quantum Tech"},
        {"url": "https://thequantuminsider.com/feed/", "category": "Quantum Tech"},
    ]

    def __init__(self):
        super().__init__()
        self.news_db = NewsDatabase()

    def fetch(self) -> List[Dict[str, Any]]:
        results = []
        logger.info(f"Scanning {len(self.FEEDS)} OSINT feeds...")
        
        for feed_config in self.FEEDS:
            url = feed_config["url"]
            category = feed_config["category"]
            try:
                feed = feedparser.parse(url)
                logger.info(f"Fetched {len(feed.entries)} items from {url}")
                
                for entry in feed.entries[:10]: # Limit to top 10 per feed to increase breadth
                    # Prepare data for both detailed storage and immediate processing
                    item_data = {
                        "url": entry.link,
                        "title": entry.title,
                        "source": url,
                        "published_date": entry.published if 'published' in entry else str(datetime.now().isoformat()),
                        "summary": entry.summary if 'summary' in entry else "",
                        "category": category
                    }
                    
                    # Archive to Persistent DB
                    self.news_db.upsert_article(item_data)

                    results.append({
                        "type": "osint_news",
                        "title": item_data["title"],
                        "link": item_data["url"],
                        "published": item_data["published_date"],
                        "summary": item_data["summary"],
                        "source": url,
                        "category": category
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch RSS {url}: {e}")
                
        return results
