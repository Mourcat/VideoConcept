from kivymd.uix.screen import MDScreen
from views.components.TubeCard.TubeCard import TubeCard
import cfg


class IntoScreen(MDScreen):
    
    
    
    def add_cards(self):
        for rec in cfg.uniquePicToCard.keys():
            self.ids.card_lay.add_widget(
            	TubeCard(
            		tube_label=rec,
            		img=cfg.uniquePicToCard.get(rec)[0],
            		outline_color=cfg.uniquePicToCard.get(rec)[1],
            		bg_color=cfg.uniquePicToCard.get(rec)[2],
            	)
            )


