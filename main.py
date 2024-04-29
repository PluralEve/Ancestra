import startup
import home
import kivy
from kivy.clock import Clock
from kivy.app import App
class startup(App):
    def __init__(self):
        startup.startup_screen()
        Clock.schedule_once(home_screen,5)
    def homescreen():
        home.home_screen()
