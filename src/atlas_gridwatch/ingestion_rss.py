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
        {"url": "https://www.datacenterdynamics.com/en/rss/", "category": "Tech & Infrastructure"},
        {"url": "https://datacenterfrontier.com/feed/", "category": "Tech & Infrastructure"},
        {"url": "https://subtelforum.com/feed/", "category": "Maritime & Cables"},
        {"url": "https://www.defenseone.com/rss/all/", "category": "Defense & Security"},
        {"url": "https://warontherocks.com/feed/", "category": "Geopolitics"},
        {"url": "https://thediplomat.com/feed/", "category": "Geopolitics"},
        {"url": "https://www.c4isrnet.com/arc/outboundfeeds/rss/", "category": "Defense & Security"},
        {"url": "https://www.csis.org/rss.xml", "category": "Defense & Security"},
        {"url": "https://foreignpolicy.com/feed", "category": "Geopolitics"}
    ]

    def fetch(self) -> List[Dict[str, Any]]:
        results = []
        logger.info(f"Scanning {len(self.FEEDS)} OSINT feeds...")
        
        for feed_config in self.FEEDS:
            url = feed_config["url"]
            category = feed_config["category"]
            try:
                feed = feedparser.parse(url)
                logger.info(f"Fetched {len(feed.entries)} items from {url}")
                
                for entry in feed.entries[:5]: # Limit to top 5 per feed to avoid noise
                    results.append({
                        "type": "osint_news",
                        "title": entry.title,
                        "link": entry.link,
                        "published": entry.published if 'published' in entry else None,
                        "summary": entry.summary if 'summary' in entry else "",
                        "source": url,
                        "category": category
                    })
            except Exception as e:
                logger.warning(f"Failed to fetch RSS {url}: {e}")
                
        return results
