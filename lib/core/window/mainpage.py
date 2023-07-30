import PySimpleGUI as sg
from .basepage import BasePage

class MainPage(BasePage):
    
    def __init__(self, title="Main Page"):
        super().__init__()
        self.title = title

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