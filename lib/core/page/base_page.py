import PySimpleGUI as sg


class BasePage:
    def __init__(self, title="Base Page"):
        # self.title が定義されていない場合は、引数の title を代入する
        if vars(self).get('title') is None:
            self.title = title

    def layout(self):
        return [
            [sg.Text('this is Base Page')],
        ]

    def export(self):
        return [self.title, self.layout]