import PySimpleGUI as sg


class BasePage:
    def __init__(self, title="Base Page"):
        self.title = title

    def layout(self):
        return [
            [sg.Text('this is Base Page')],
        ]

    def export(self):
        return [self.title, self.layout]