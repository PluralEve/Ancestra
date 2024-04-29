from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp

class ContentNavigationDrawer(BoxLayout):
    pass

class TestNavigationDrawerApp(App):
    def build(self):
        sm = ScreenManager()

        # Main screen
        main_screen = Screen(name='main')
        main_layout = BoxLayout(orientation='vertical')

        # Top app bar
        top_app_bar = BoxLayout(size_hint_y=None, height=dp(56))
        top_app_bar.add_widget(Button(text='Menu', size_hint=(None, 1)))
        top_app_bar.add_widget(Label(text='ANCESTRA'))

        # Content navigation drawer
        content_navigation_drawer = ContentNavigationDrawer(orientation='vertical', spacing=dp(8), padding=dp(8))
        content_navigation_drawer.add_widget(Label(text="programs"))
        for i in range(1, 10):
            content_navigation_drawer.add_widget(Label(text=f"Item {i}"))

        # Add widgets to main layout
        main_layout.add_widget(top_app_bar)
        main_layout.add_widget(content_navigation_drawer)

        # Add main layout to main screen
        main_screen.add_widget(main_layout)

        # Add main screen to screen manager
        sm.add_widget(main_screen)

        return sm

if __name__ == '__main__':
    TestNavigationDrawerApp().run()



