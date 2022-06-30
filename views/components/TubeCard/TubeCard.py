from kivy.clock import Clock
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from pytube import YouTube


class TubeCard(MDCard):
    yt_url = StringProperty()
    tube_label = StringProperty()
    img = StringProperty('C:/Users/Виктор Выборнов/Pictures/T9OiwUchG78.jpg')

    def dl_callback(self, dt):
        self.ids.info_lbl.theme_text_color = 'Custom'
        self.ids.info_lbl.text_color = MDApp.get_running_app().theme_cls.primary_light
        self.ids.info_lbl.text = 'Please, paste YouTube url?!'
        
    def download_it(self, yt_url):
        app = MDApp.get_running_app()
        try:
            yt_obj = YouTube(yt_url)
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download()
            self.ids.info_lbl.theme_text_color = 'Custom'
            self.ids.info_lbl.text_color = app.theme_cls.accent_color
            self.ids.info_lbl.text = 'Successfully!'
            Clock.schedule_once(self.dl_callback, 3)     
        except Exception as e:
            self.ids.info_lbl.theme_text_color = 'Error'
            self.ids.info_lbl.text = 'Something wrong!'
            Clock.schedule_once(self.dl_callback, 3)
