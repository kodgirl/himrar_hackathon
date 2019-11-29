from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', "400")
Config.set('graphics', 'height', "600")

#class TopApp(App):
def build(self):
    print('lol')
    self.Al = AnchorLayout()
    cam = Camera(resolution = (320, 240), play = True)
    self.Al.add_widget(cam)
    return self.Al

#TopApp().run()
