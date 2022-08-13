"""
The queuer of dreams.
"""
import toga
import pyaudio
import wave
from .components import Feed, Episode
from urllib.request import urlopen
from playsound import playsound
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Podcaster(toga.App):
    def startup(self):
        main_box = toga.Box()

        feed = Feed('http://feed.thisamericanlife.org/talpodcast')
        up_next_ep = feed.up_next()
        # TODO: player(feed) -> plays the next episode from the feed

        feed_box = toga.Box()
        feed_box.add(toga.Label(feed.title, style = Pack(direction=ROW, padding=5)))
        feed_box.add(toga.Label(up_next_ep.title, style=Pack(direction=ROW, padding=5)))

        main_box.add(feed_box)


        # self.is_paused = True
        # play_switch = toga.Switch('Play/pause', is_on=self.is_paused, style=Pack(padding=5), on_toggle=self.handle_play_button)
        # main_box.add(play_switch)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def handle_play_button(self, widget):
        self.is_paused = not self.is_paused
        while not self.is_paused:
            self.alt_play()
        return None

    def play(self):
        print('play')
        with open('./test.mp3','wb') as output:
            output.write(urlopen(self.ep_audio_url).read())
        playsound('./test.mp3')
        return None
    
    def alt_play(self):
        pyaud = pyaudio.PyAudio()
        srate=44100
        stream = pyaud.open(format = pyaud.get_format_from_width(1),
                        channels = 1,
                        rate = srate,
                        output = True)
        u = urlopen(self.ep_audio_url)
        data = u.read(8192)

        while data:
            stream.write(data)
            data = u.read(8192)
        print('alt_play')
        


def main():
    return Podcaster(name='Podcaster', app_id='cz.vgg.podcaster')
