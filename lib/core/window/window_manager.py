import PySimpleGUI as sg
import threading

from .mainpage import MainPage

# 管理ウィンドウの管理クラス
class WindowManager:

    # ウィンドウ初期化
    def __init__(self, stop_callback=None):
        self.buttons_map = {}
        #self.title = title
        #self.layout = layout
        self.window = None
        self.thread = None
        self.layouts = [
            # ["全般", lambda: [sg.Text('正常に起動しました。')]],
            # ["認証", lambda: [sg.Text('認証済みです。')]],
            # ["バージョン情報", lambda: [sg.Text('simple exe version 1.0.0')]],
            # ["クレジット", lambda: [sg.Text('made by sawai')]]
        ]
        self.stop_callback = stop_callback

    # ウィンドウ起動
    def start(self):
        self.thread = threading.Thread(target=self.create_window)
        self.thread.start()
        return self.thread

    # ウィンドウ起動
    def create_window(self):

        # ウィンドウが既に起動している場合は起動せず、既存のウィンドウを前面に表示する
        if self.window is not None:
            # self.window.bring_to_front()
            return
        self.window_refresh = False

        # テーマの設定
        sg.theme('Default1')

        # ベースのレイアウト
        layout = [
            [sg.Button(button_text=f"{layout[0]}", key=f'{i}') for i, layout in enumerate(self.layouts)],
            [sg.Column([layout[1]()], key=f'-COL{i}-', visible=(i==0), size=(400, 140), pad=(0, 0)) for i, layout in enumerate(self.layouts)],
            [sg.Button(key="OK", button_text="OK"), sg.Button(key="Cancel", button_text="閉じる"), sg.Button(key='Shutdown', button_text="終了")]
        ]

        # ウィンドウを作成
        self.window = sg.Window('Window Title', layout, size=(400, 200), margins=(0,0))

        # ウィンドウ表示ループ
        layout_number = 0
        while True:
            event, values = self.window.read(timeout=1000, timeout_key='window-read-timeout')
            print(event, values)

            if event == 'window-read-timeout':
                if self.window_refresh:
                    self.window_refresh = False
                    break
                continue

            if event == 'OK':
                print('OK')

            # レイアウト切り替えイベント
            if event in [str(i) for i in range(len(self.layouts))]:
                self.window[f'-COL{layout_number}-'].update(visible=False)
                self.window[f'-COL{event}-'].update(visible=True)
                layout_number = int(event)

            # ウィンドウを閉じるかキャンセルボタンが押された場合はループを抜ける
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            # 終了ボタンが押された時はタスクトレイのプロセスも終了してループを抜ける
            if event == 'Shutdown':
                self.stop_callback()
                break
        
        # ウィンドウを閉じる
        self.window.close()
        self.window = None

    # ページを追加する
    def add_page(self, page):
        self.layouts.append(page.export())


    def stop(self):
        self.window_refresh = True