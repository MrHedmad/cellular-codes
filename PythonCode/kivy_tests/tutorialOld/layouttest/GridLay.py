from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class GridLayApp(App):

    def build(self):
        return GridLayout()


GridLayApp().run()
