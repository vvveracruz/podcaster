import requests
from pygame import mixer
from io import BytesIO


class Player:
    def __init__(self, feed):
        self._feed = feed
        self._player = None

    @property
    def player(self):
        if self._player is None:
            self._player = self.player_from_url(self._feed.up_next().audio_url)
        return self._player

    def player_from_url(self, url):
        mixer.init()
        r = requests.get(url, stream=True)
        stream = BytesIO(r.raw.read())

        mixer.music.load(stream)

        return mixer.music
