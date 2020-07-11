from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class multiplescreensApp(App):
    def build(self):
        pass


if __name__ == "__main__":
    multiplescreensApp().run()
