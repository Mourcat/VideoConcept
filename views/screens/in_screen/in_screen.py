from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from pytube import YouTube
from views.components.TubeCard.TubeCard import TubeCard


class IntoScreen(MDScreen):
    
    tube_names = [
        'YouTube Downloader',
        'PornHub Downloader'
    ]
    
    def add_cards(self):
        for name in self.tube_names:
            self.ids.card_lay.add_widget(TubeCard(tube_label=name))


