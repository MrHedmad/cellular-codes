from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class CustomGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def button(self):
        print("Name: {}, Email: {}".format(self.name.text, self.email.text))
        self.name.text = ""
        self.email.text = ""


class tutorialApp(App):
    def build(self):
        return CustomGrid()


if __name__ == "__main__":
    tutorialApp().run()
