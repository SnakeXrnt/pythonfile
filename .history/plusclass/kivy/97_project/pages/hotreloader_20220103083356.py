from kivy.lang import Builder
from kivy.config import Config
from kivymd.app import MDApp

WIDTH= 9*40
HEIGHT = 16*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer


BoxLayout:

    HotReloadViewer:
        size_hint_x: .2
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 0, 0, 1
        errors_background_color: app.theme_cls.bg_light
'''


class Example(MDApp):
    path_to_kv_file = "daashb.kv"

    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)
            

Example().run()