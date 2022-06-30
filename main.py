from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from views import IntoScreen, TubeCard


class YLoaderApp(MDApp):
    
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.material_style = 'M3'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Green'
        self.kvs_loader()
        self.root = IntoScreen()
        return self.root
        
    def on_start(self):
        self.root.add_cards()
        
    def kvs_loader(self):
        Builder.load_file('views/screens/in_screen/in_screen.kv')
        Builder.load_file('views/components/TubeCard/TubeCard.kv')        
        
        
if __name__ == '__main__':
    YLoaderApp().run()