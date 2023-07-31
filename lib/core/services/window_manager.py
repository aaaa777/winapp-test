import PySimpleGUI as sg
import threading

from ..utils import Consts
from ..service import BaseService

# 管理ウィンドウの管理クラス
class WindowManager(BaseService):

    # ウィンドウ初期化
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window = None
        self.layouts = []

    # バックグラウンド無効化
    def run(self):
        pass

    # ウィンドウ起動
    def create_window(self):
        return threading.Thread(target=self.create_window_thread).start()

    # Thread用ウィンドウ起動
    def create_window_thread(self):

        # ウィンドウが既に起動している場合は起動せず、既存のウィンドウを前面に表示する
        if self.window is not None:
            self.window.bring_to_front()
            return
        self.window_refresh = False

        window_width = Consts.window_width
        window_height = Consts.window_height
        image_data = Consts.px_image_data

        # テーマの設定
        sg.theme('SystemDefaultForReal')

        # ベースのレイアウト
        sg.set_options(element_padding=(0, 0))

        # ヘッダーの列数調整
        for i in range(4-(len(self.layouts)%4)):
            self.layouts.append([None, lambda: []])

        # ヘッダーに⇔ボタンを追加
        header_layouts = [sg.Button(key=f"-COL-PREV0-", button_text="←", image_data=image_data, image_size=(25, 15), pad=(0, 0), disabled=True)]
        for i in range(len(self.layouts)):
            header_layouts.append(sg.Button(button_text=f"{' ' if self.layouts[i][0] is None else self.layouts[i][0]}", key=f'{i}', image_data=image_data, image_size=(80, 15), disabled=self.layouts[i][0] is None, pad=(0, 0), tooltip=self.layouts[i][0]))
            if i % 4 == 3:
                header_layouts.append(sg.Button(key=f"-COL-NEXT{i//4}-", button_text="→", image_data=image_data, image_size=(25, 15), pad=(0, 0), disabled=(i+1==len(self.layouts))))
                header_layouts.append(sg.Button(key=f"-COL-PREV{(i//4)+1}-", button_text="←", image_data=image_data, image_size=(25, 15), pad=(0, 0)))
        
        del header_layouts[-1]

        print(header_layouts)
        window_layout = [
            # [sg.Column([[sg.Button(button_text=f"{layout[0]}", key=f'{i}', image_data=image_data, image_size=(80, 15)) for i, layout in enumerate(self.layouts)]], key="COL-topbar", scrollable=False, size=(window_width + 20, None), pad=(0, 0))],
            [sg.Column([header_layouts], key="COL-topbar", scrollable=False, size=(window_width, 20), pad=(0, 0))],
            [sg.Column((print(layout) is True) or [layout[1]()], key=f'-COL{i}-', visible=(i==0), size=(window_width, 150), pad=(0, 0)) for i, layout in enumerate(self.layouts)],
            [sg.Button(key="OK", button_text="OK"), sg.Button(key="Cancel", button_text="閉じる"), sg.Button(key='Shutdown', button_text="終了")]
        ]

        # ウィンドウを作成
        self.window = sg.Window('Window Title', window_layout, size=(window_width, window_height), margins=(0,0))

        # self.window["COL-topbar"].Widget.vscrollbar.pack_forget()

        # ウィンドウ表示ループ
        layout_number = 0
        header_number = 0
        while True:
            event, values = self.window.read(timeout=1000, timeout_key='window-read-timeout')
            print(event, values)

            if event == 'window-read-timeout':
                if self.window_refresh:
                    self.window_refresh = False
                    break
                continue

            # OKボタンが押された場合はOKを表示
            if event == 'OK':
                print('OK')

            # ウィンドウを閉じるかキャンセルボタンが押された場合はループを抜ける
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            # レイアウト切り替えイベント
            if event in [str(i) for i in range(len(self.layouts))]:
                self.window[f'-COL{layout_number}-'].update(visible=False)
                self.window[f'-COL{event}-'].update(visible=True)
                layout_number = int(event)

            # ヘッダーの矢印ボタンイベント
            if "-COL-NEXT" in event:
                self.window[f'-COL-PREV{header_number}-'].update(visible=False)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=False)
                self.window[f'{header_number*4+0}'].update(visible=False)
                self.window[f'{header_number*4+1}'].update(visible=False)
                self.window[f'{header_number*4+2}'].update(visible=False)
                self.window[f'{header_number*4+3}'].update(visible=False)
                header_number += 1
                self.window[f'-COL-PREV{header_number}-'].update(visible=True)
                self.window[f'{header_number*4+0}'].update(visible=True)
                self.window[f'{header_number*4+1}'].update(visible=True)
                self.window[f'{header_number*4+2}'].update(visible=True)
                self.window[f'{header_number*4+3}'].update(visible=True)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=True)

            if "-COL-PREV" in event:
                self.window[f'-COL-PREV{header_number}-'].update(visible=False)
                self.window[f'{header_number*4+0}'].update(visible=False)
                self.window[f'{header_number*4+1}'].update(visible=False)
                self.window[f'{header_number*4+2}'].update(visible=False)
                self.window[f'{header_number*4+3}'].update(visible=False)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=False)
                header_number -= 1
                self.window[f'-COL-PREV{header_number}-'].update(visible=True)
                self.window[f'{header_number*4+0}'].update(visible=True)
                self.window[f'{header_number*4+1}'].update(visible=True)
                self.window[f'{header_number*4+2}'].update(visible=True)
                self.window[f'{header_number*4+3}'].update(visible=True)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=True)

            # 終了ボタンが押された時はタスクトレイのプロセスも終了してループを抜ける
            if event == 'Shutdown':
                if self.stop_callback is not None:
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