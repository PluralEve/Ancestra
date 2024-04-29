from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp

KV = '''
Screen:

    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "ANCESTRA"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]

        MDNavigationDrawer:
            id: nav_drawer
            width: dp(230)  # Adjust drawer width for mobile

            ContentNavigationDrawer:
                orientation: 'vertical'
                spacing: dp(8)
                padding: dp(8)  # Add padding to the content

                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height  # Adjust the height dynamically

                    OneLineListItem:
                        text: "programs"
                    OneLineListItem:
                        text: "Item 2"
                    OneLineListItem:
                        text: "Item 1"
                    OneLineListItem:
                        text: "Item 2"
                    OneLineListItem:
                        text: "Item 1"
                    OneLineListItem:
                        text: "Item 2"
                    OneLineListItem:
                        text: "Item 1"
                    OneLineListItem:
                        text: "Item 2"
                    OneLineListItem:
                        text: "Item 1"
                    OneLineListItem:
                        text: "Item 2"
'''

class ContentNavigationDrawer(BoxLayout):
    pass

class TestNavigationDrawer(MDApp):
    def build(self):
        root = Builder.load_string(KV)
        # Initially close the navigation drawer
        root.ids.nav_drawer.set_state('close')
        return root
def home_screen():
    TestNavigationDrawer().run()