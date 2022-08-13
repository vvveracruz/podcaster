import feedparser as fp
from toga import Label
from toga.style import Pack

class Feed():
    def __init__(self, url_file_stream_or_string):
        self._feed = fp.parse(url_file_stream_or_string)
    
    # TODO: explode these programmatically
    @property
    def title(self):
        return self._feed.feed.title
    
    @property
    def entries(self):
        return self._feed.entries

    def up_next(self):
        # TODO: handle reordering here
        return self._feed.entries[0]

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
