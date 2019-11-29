from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import cv2, os, good
from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
#from PIL import Image as ime
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', "400")
Config.set('graphics', 'height', "600")

class TopApp(App):
    def end(self, instance):
        al = AnchorLayout()
        lal= BoxLayout(orientation='vertical')

        al.add_widget(Button(text='', background_normal='', background_color=[1,1,1,1]))
        bl = BoxLayout(orientation='vertical', padding=[50], spacing=8)
        wmimg = Image(source='photo/' + str(instance.text))
        widget = Widget()
        with widget.canvas:
            widget = wmimg
        bl.add_widget(Widget())
        lal.add_widget(widget)
        lal.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        if (good.my_func(wmimg) == 0):
            bl.add_widget(Label(text='some error, pls try again', color=[0,1,1,1]))
            time.sleep(5)
            exit()
        instance.text = good.ret_smiles()
        bl.add_widget(Label(text='SMILES:', color=[0,0,0,1]))
        bl.add_widget(Button(text=str(instance.text), color=[0,0,0,1], background_normal='', background_color=[0, 1, 0, 1]))
        bl.add_widget(Button(text="Главное меню", color=[.1, .1, .1, 1], background_normal='', background_color=[.5,.5,.5, 1]))
        self.Al.add_widget(al)
        self.Al.add_widget(lal)
        self.Al.add_widget(bl)
        return self.Al

    def replay(self, instance):
        screen = Window.screenshot('screen.png')
        srce = str(screen)
        for i in srce:
            i = srce
        x = srce.split("/")
        self.str = x[len(x) - 1]
        al = AnchorLayout()
        lal= BoxLayout(orientation='vertical')

        al.add_widget(Button(text='', background_normal='', background_color=[1,1,1,1]))
        bl = BoxLayout(orientation='vertical', padding=[50], spacing=8)
        wmimg = Image(source='photo/images.png')
        widget = Widget()
        with widget.canvas:
            widget = wmimg
        bl.add_widget(Widget())
        lal.add_widget(widget)
        lal.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Label(text='SMILES:', color=[0,0,0,1]))
        bl.add_widget(Button(text='здесь должен быть SMILES', color=[0,0,0,1], background_normal='', background_color=[0, 1, 0, 1]))
        bl.add_widget(Button(text="Главное меню", color=[.1, .1, .1, 1], background_normal='', background_color=[.5,.5,.5, 1]))
        self.Al.add_widget(al)
        self.Al.add_widget(lal)
        self.Al.add_widget(bl)
        return self.Al

    def find(self, instance):
        ll = AnchorLayout()
        al = AnchorLayout()
        al.add_widget(Button(text='', background_normal='', background_color=[1,1,1,1]))
        bl = BoxLayout(orientation='vertical', padding=[50], spacing=8)
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        ll.add_widget(Button(text=' ',  background_normal='', background_color=[0,0,0,1]))
        bl.add_widget(Button(text="Сделать фотографию", color=[.1, .1, .1, 1], on_press = self.replay ,background_normal='',  background_color =[.5, .5, .5, 1]))
        self.cam = Camera(resolution = (320, 240), play = True)
        al.add_widget(self.cam)
        ll.add_widget(al)
        self.Al.add_widget(ll)
        self.Al.add_widget(bl)
        return self.Al

    def readf(self, instance):
        print(str(instance.text))
        return self.Al

    def ffind(self, instance):
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', padding=[50], spacing=8)
        for i in range(len(self.files)):
            bl.add_widget(Button(text=self.files[i], on_press= self.end))
        self.Al.add_widget(al)
        self.Al.add_widget(bl)
        print(len(self.files))
        return self.Al

    def build(self):
        self.Al = AnchorLayout()
        path = os.getcwd()
        if os.path.exists('photo'):
            pass
        else:
            os.mkdir('photo')
        self.files = os.listdir('photo')
        wmimg = Image(source='logo.png')
        imimg = Image(source='first.jpg')
        widget = Widget()
        with widget.canvas:
            widget = wmimg
        iidget = Widget()
        with iidget.canvas:
            iidget = imimg
        al = AnchorLayout()
        bl = BoxLayout(orientation='vertical', padding=[50], spacing=8)
        self.Al.add_widget(Button(text=' ', background_normal='', background_color=[1, 1, 1, 1]))
        al.add_widget(iidget)
        bl.add_widget(widget)
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Widget())
        bl.add_widget(Button(text="Нажмите, чтобы сделать фото", color=[.1, .1, .1, 1], on_press = self.find ,background_normal='',  background_color =[.5, .5, .5, 1]))
        bl.add_widget(Button(text="Нажмите, чтобы найти фото", color=[.1, .1, .1, 1] , on_press = self.ffind, background_normal='', background_color = [.5, .5, .5, 1])) 
        al.add_widget(bl)
        self.Al.add_widget(al)
        return self.Al

if __name__ == "__main__":
    TopApp().run()
