import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Привет, это мое первое приложение!", font_size='30sp')

if __name__ == '__main__':
    MyApp().run()
