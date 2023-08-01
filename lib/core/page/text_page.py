import PySimpleGUI as sg
from .managed_page import ManagedPage

class TextPage(ManagedPage):
    
    def __init__(self, header=None, text="sample text", **kwargs):
        super().__init__(**kwargs)
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