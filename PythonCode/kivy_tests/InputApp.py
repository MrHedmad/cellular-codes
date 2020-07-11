from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse touched @: ", touch)
        self.btn.opacity = 0.5

    def on_touch_up(self, touch):
        print("Mouse left @: ", touch)
        self.btn.opacity = 1

    def on_touch_move(self, touch):
        print("Mouse moved to: ", touch)


class InputApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    InputApp().run()
