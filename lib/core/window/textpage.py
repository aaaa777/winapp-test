import PySimpleGUI as sg
from .basepage import BasePage

class TextPage(BasePage):
    
    def __init__(self, title="Text Page", header=None, text="sample text"):
        super().__init__()
        self.title = title
        self.header = header
        self.text = text

    def layout(self):
        rows = []

        if self.header:
            rows.append([sg.Text(self.header)])

        rows.append([sg.Text(self.text)])

        return [
            sg.Column(rows, scrollable=True, vertical_scroll_only=True, size=(380, 140), pad=(0, 0)),
        ]