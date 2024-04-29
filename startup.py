from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.config import Config
from kivy.graphics import Rectangle
import home

Config.set('kivy', 'default_font', ['fonts/Roboto-Regular.ttf'])

class ImageBackground(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(source='images/background.jpeg', pos=self.pos, size=self.size)

    def on_size(self, *args):
        self.rect.size = self.size 

class StartupScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logo = Image(source='logo.png', size_hint=('0.75', '0.75'), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.logo)
        self.add_widget(Label(text="Universal Public School", font_size='15sp', size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.9}, color=(0,0,0,0.7)))
        self.label = Label(text="Welcome", font_size='50sp', size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.7}, color=(0,0,0,1))
        self.label.font_name='fonts\MontserratAlternates-Bold.ttf'
        self.add_widget(self.label)

class AncestraApp(App):
    def build(self):
        self.title = 'My App'
        root = FloatLayout()
        bg = ImageBackground()
        startup_screen = StartupScreen()
        
        # Add widgets to the root layout with specific positions
        root.add_widget(bg)
        root.add_widget(startup_screen)

        Clock.schedule_once(self.switch_to_next_screen, 3)
        return root

    def switch_to_next_screen(self, dt):
        print("Switching to the main screen...")
def startup_screen():
    if __name__ == '__main__':
        AncestraApp().run()
