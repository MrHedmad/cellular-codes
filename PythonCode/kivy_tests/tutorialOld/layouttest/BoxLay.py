from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayApp(App):

    def build(self):
        return BoxLayout()


BoxLayApp().run()
