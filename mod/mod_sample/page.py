from PySimpleGUI import PySimpleGUI as sg
from lib.core.page import BasePage

class SampleModPage(BasePage):

    layout = [
        [sg.Text('Sample Mod Window')],
    ]
    
    def __init__(self):
        super().__init__()

        self._window = None