import PySimpleGUI as sg
from ..page.managed_page import ManagedPage

class MainPage(ManagedPage):
    
    def __init__(self, **kwargs):
        # self.titleはsuper().__init__の前に設定する
        self.title = "Main Page"
        super().__init__(**kwargs)

    def layout(self):
        return [
            sg.Column([
                [
                    sg.Text('This is Main Page')
                ],
                [
                    sg.Text('This is Main Page')
                ],
                [
                    sg.Text('This is Main Page')
                ],
                [
                    sg.Button(key="Main-OK", button_text="OK"), sg.Button(key="Main-Cancel", button_text="キャンセル")
                ],
                [
                    sg.Button(key="Main-OK", button_text="OK"), sg.Button(key="Main-Cancel", button_text="キャンセル")
                ],
                [
                    sg.Button(key="Main-OK", button_text="OK"), sg.Button(key="Main-Cancel", button_text="キャンセル")
                ],
                [
                    sg.Button(key="Main-OK", button_text="OK"), sg.Button(key="Main-Cancel", button_text="キャンセル")
                ],
            ], scrollable=True, vertical_scroll_only=True, size=(380, 140), pad=(0, 0)),
        ]