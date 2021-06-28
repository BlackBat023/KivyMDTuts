from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder

list_helper = """
Screen: 
    ScrollView:
        MDList:
            id: container

"""

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            item = OneLineListItem(text='Item ' + str(i))
            self.root.ids.container.add_widget(item)


DemoApp().run()
