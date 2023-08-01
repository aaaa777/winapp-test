from PySimpleGUI import PySimpleGUI as sg
from lib.core.page import ManagedPage

class SampleModPage(ManagedPage):

    def __init__(self, **kwargs):
        kwargs['title'] = "MODサンプル"
        super().__init__(**kwargs)

    def layout(self):
        return [
            sg.Column([[sg.Text('Sample Mod Window')]], scrollable=True, vertical_scroll_only=True, size=(380, 140), pad=(0, 0)),
        ]
