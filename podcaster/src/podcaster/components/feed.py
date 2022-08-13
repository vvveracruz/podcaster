import feedparser as fp
from toga import Label
from toga.style import Pack

class Episode():
    def __init__(self, data):
        self._data = data
        self._audio_url = None
    
    # TODO: explode these programmatically
    @property
    def title(self):
        return self._data.title
    
    @property
    def audio_url(self):
        if self._audio_url == None:
          for i in self._data.links:
              if i.type == 'audio/mpeg':
                  self._audio_url=i.href
        return self._audio_url

# TODO: generalise feed to be a queue or a podcast feed
class Feed():
    def __init__(self, url_file_stream_or_string):
        self._feed = fp.parse(url_file_stream_or_string)
    
    # TODO: explode these programmatically
    @property
    def title(self):
        return self._feed.feed.title

    def up_next(self):
        # TODO: handle reordering here
        return Episode(self._feed.entries[0])
