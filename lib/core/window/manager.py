import PySimpleGUI as sg
import threading

from .main import MainWindow

class WindowManager:
    def __init__(self):
        self.buttons_map = {}
        #self.title = title
        #self.layout = layout
        #self.window = sg.Window(self.title, self.layout)
        self.thread = threading.Thread(target=self.start)
        self.layouts = [
            lambda: ["全般", [sg.Text('正常に起動しました。')]],
            lambda: ["認証", [sg.Text('認証済みです。')]],
            lambda: ["バージョン情報", [sg.Text('simple exe version 1.0.0')]],
            lambda: ["クレジット", [sg.Text('made by sawai')]]
        ]

    def start(self, stop_callback=None):

        sg.theme('Default1')

        layout = [
            [sg.Button(button_text=f"{layout()[0]}", key=f'{i}') for i, layout in enumerate(self.layouts)],
            [sg.Column([layout()[1]], key=f'-COL{i}-', visible=(i==0)) for i, layout in enumerate(self.layouts)],
            [sg.Button(key="OK", button_text="OK"), sg.Button(key="Cancel", button_text="キャンセル"), sg.Button(key='Shutdown', button_text="アプリを終了")]
        ]

        window = sg.Window('Window Title', layout)

        layout_number = 0
        while True:
            event, values = window.read()
            print(event, values)
            if event in [str(i) for i in range(len(self.layouts))]:
                window[f'-COL{layout_number}-'].update(visible=False)
                window[f'-COL{event}-'].update(visible=True)
                layout_number = int(event)

            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            if event == 'Shutdown':
                window.close()
                stop_callback()
                break
        
        window.close()

    def open(self, window):
        self.windows.append(window)

    def wait(self):
        self.thread.join()