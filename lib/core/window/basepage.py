import PySimpleGUI as sg


class BasePage:
    def __init__(self):
        self.title = "Base Page"

    def export(self):
        return [self.title, lambda: [sg.Text('this is Base Page')]]