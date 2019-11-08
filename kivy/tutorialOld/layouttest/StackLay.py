from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class StackLayApp(App):

    def build(self):
        return StackLayout()


StackLayApp().run()
