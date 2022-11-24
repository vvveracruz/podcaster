from typing import Iterable
from feedparser import parse
from feedparser.util import FeedParserDict
import json


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
    # TODO: is comparing titles really the best way to do this?
    # Maybe unique key from published time and name?
    while ep["title"] in [ep["title"] for ep in listening_history]:
        ep = next(entries)
    return ep


# build queue from json file of rss feed links

# scrape itunes/ web in general to get rss feed link from name

_planet_money_rss = "https://feeds.npr.org/510289/podcast.xml"
d = parse(_planet_money_rss)
with open("history.json") as f:
    history = json.load(f)
print(get_next_episode(d, history, "latest")["title"])
# print(type(d['entries'][0]))
