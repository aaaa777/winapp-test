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
            lambda: [sg.Text('test layout 1')],
            lambda: [sg.Text('test layout 2')],
            lambda: [sg.Text('test layout 3')],
            lambda: [sg.Text('test rwest 4')]
        ]

    def start(self, stop_callback=None):

        sg.theme('DarkAmber')

        layout = [
            [sg.Text('My one-shot window.')],
            [sg.Button(f'{i}') for i in range(len(self.layouts))],
            [sg.Column([layout()], key=f'-COL{i}-', visible=(i==0)) for i, layout in enumerate(self.layouts)],
            [sg.Submit(), sg.Cancel(), sg.Button('Shutdown')]
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