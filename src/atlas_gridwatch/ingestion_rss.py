import feedparser
import logging
from typing import List, Dict, Any
from .ingestion import BaseIngestor

logger = logging.getLogger(__name__)

class RSSIngestor(BaseIngestor):
    """
    Ingests OSINT from industry RSS feeds.
    """
    
    FEEDS = [
        "https://www.datacenterdynamics.com/en/rss/",
        "https://datacenterfrontier.com/feed/",
        "https://feeds.feedburner.com/DataCenterKnowledge"
    ]

    def fetch(self) -> List[Dict[str, Any]]:
        results = []
        logger.info(f"Scanning {len(self.FEEDS)} OSINT feeds...")
        
        for url in self.FEEDS:
            try:
                feed = feedparser.parse(url)
                logger.info(f"Fetched {len(feed.entries)} items from {url}")
                
                for entry in feed.entries[:10]: # Limit to top 10 per feed
                    results.append({
                        "type": "osint_news",
                        "title": entry.title,
                        "link": entry.link,
                        "published": entry.published if 'published' in entry else None,
                        "summary": entry.summary if 'summary' in entry else "",
                        "source": url
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch RSS {url}: {e}")
                
        return results
