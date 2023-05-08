import json
from typing import Iterable

from feedparser import parse
from feedparser.util import FeedParserDict

class Entity():
    def __init__(self, entity_dict: dict):

class Queue():
    def __init__(self, feed_url: str):
        self._feed_url = feed_url
        self._feed_dict = parse(self._feed_url)
        self._entries = self._feed_dict['entries']
    
    @property
    def feed_dict(self):
        # TODO: handle parsing urls that aren't identical to the rss feed
        return self._feed_dict 

    @property
    def entries(self):
        return self._entries
        
pod = Queue('https://feeds.buzzsprout.com/2040953.rss')
print(pod.feed_dict.keys())
print(len(pod.entries))

def get_next_episode(
    feed: FeedParserDict,
    listening_history: Iterable[FeedParserDict],
    oldest_last: bool = True,
) -> FeedParserDict:
    if oldest_last:
        # get next up from top of feed (most recent)
        entries = iter(feed["entries"])
    else:
        # get next up from top of bottom of feed (oldest)
        entries = iter(feed["entries"][::-1])
    ep = next(entries)
    # skip listened episodes
    # TODO: is comparing titles really the best way to do this?
    # Maybe unique key from published time and name?
    while ep["title"] in [ep["title"] for ep in listening_history]:
        ep = next(entries)
    return ep


# build queue from json file of rss feed links

# scrape itunes/ web in general to get rss feed link from name
