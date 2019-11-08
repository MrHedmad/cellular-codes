from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager


class IntroductionWindow(Screen):
    pass


class MeltVCFWindow(Screen):
    pass


class ExtractChasmWindow(Screen):
    pass


class CrystalWindow(Screen):
    pass


class CoOccurrenceWindow(Screen):
    pass


class AdvancedWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainGridLayout(GridLayout):
    pass


class ScreenSwitcher(GridLayout):
    pass


class MuaApp(App):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    MuaApp().run()
