from kivymd.uix.screen import MDScreen
from views.components.TubeCard.TubeCard import TubeCard


class IntoScreen(MDScreen):
    
    tube_names = [
        'YouTube Downloader',
        'PornHub Downloader',
        'EPorner',
    ]
    
    def add_cards(self):
        for name in self.tube_names:
            self.ids.card_lay.add_widget(TubeCard(tube_label=name))


