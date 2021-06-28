from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Dark"
        label = MDLabel(text="Hello World", halign='center', theme_text_color='Custom',
                        text_color=(236/255.0, 98/255.0, 81/255.0, 1),
                        font_style='Caption')
        icon_label = MDIcon(icon='language-csharp', halign='center')
        screen = Screen()
        # btn_flat = MDRectangleFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        icon_btn = MDFloatingActionButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(icon_btn)
        return screen


DemoApp().run()