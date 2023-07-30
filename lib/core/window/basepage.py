import PySimpleGUI as sg


class BasePage:
    def __init__(self):
        self.title = "Base Page"

    def layout(self):
        return [
            [sg.Text('this is Base Page')],
        ]

    def export(self):
        return [self.title, self.layout]