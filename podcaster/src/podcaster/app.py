"""
The queuer of dreams.
"""
import toga
from .components import Feed
from .components import Player
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from time import sleep


class Podcaster(toga.App):
    def startup(self):
        main_box = toga.Box()

        feed = Feed("http://feed.thisamericanlife.org/talpodcast")
        up_next_ep = feed.up_next()

        feed_box = toga.Box()
        feed_box.add(toga.Label(feed.title, style=Pack(direction=ROW, padding=5)))
        feed_box.add(toga.Label(up_next_ep.title, style=Pack(direction=ROW, padding=5)))
        main_box.add(feed_box)

        self.player = Player(feed).player

        self.is_first_click = True
        self.is_paused = False
        play_switch = toga.Switch(
            "Play/pause",
            is_on=self.is_paused,
            style=Pack(padding=5),
            on_toggle=self.handle_play_button,
        )
        main_box.add(play_switch)

        self.main_window = toga.MainWindow(title=self.name)
        self.main_window.content = main_box
        self.main_window.show()

    def handle_play_button(self, widget):
        if self.is_first_click:
            self.player.play()
            self.is_first_click = False
        else:
            self.is_paused = not self.is_paused
            if self.is_paused:
                self.player.pause()
            else:
                self.player.unpause()
        return None


def main():
    # return Podcaster(name="Podcaster", app_id="cz.vgg.podcaster")
    return Podcaster()
