
from PySimpleGUI import PySimpleGUI as sg
from lib.core.window.base import BaseWindow

class SampleModWindow(BaseWindow):

    layout = [
        [sg.Text('Sample Mod Window')],
    ]
    
    def __init__(self):
        super().__init__()

        self._window = None