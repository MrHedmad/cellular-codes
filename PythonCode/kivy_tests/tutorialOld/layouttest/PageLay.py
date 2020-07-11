from kivy.app import App
from kivy.uix.pagelayout import PageLayout


class PageLayApp(App):

    def build(self):
        return PageLayout()


PageLayApp().run()
