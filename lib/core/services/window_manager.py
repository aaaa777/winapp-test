import PySimpleGUI as sg
import threading
import win32gui

from ..service import FunctionService
from ..page import ManagedPage, NonePage

# 管理ウィンドウの管理クラス
class WindowManager(FunctionService):

    init = None

    # ウィンドウ初期化
    def __init__(self, window_width=400, window_height=200, page_title_width=80, page_title_height=15, **kwargs):
        # 既に初期化済みの場合は既存のインスタンスを返す
        if not WindowManager.init is None:
            raise Exception("WindowManager is already initialized. use WindowManager.init")
        
        super().__init__(**kwargs)
        self.window_width = window_width
        self.window_height = window_height
        self.page_title_width = page_title_width
        self.page_title_height = page_title_height
        self.layouts = []

        self.window = None
        self.window_refresh = False
        
        self.px_image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'
        ManagedPage.manager = self

        WindowManager.init = self


    # ページを追加する
    def add_page(self, page):
        self.layouts.append(page.export())


    # ウィンドウ起動
    def create_window(self):
        return threading.Thread(target=self.create_window_thread).start()
    

    # Thread用ウィンドウ起動
    def create_window_thread(self):

        # ウィンドウが既に起動している場合は起動せず、既存のウィンドウを前面に表示する
        if self.window is not None:
            self.window.bring_to_front()
            win32gui.SetForegroundWindow(self.window.TKroot.winfo_id())
            return
            # while self.window is not None:
            #     self.window_refresh = True
        
        self.window_refresh = False

        window_width  = self.window_width
        window_height = self.window_height
        page_title_width  = self.page_title_width
        page_title_height = self.page_title_height
        scroll_button_width  = (window_width - page_title_width * 4 - 30) // 2
        image_data    = self.px_image_data

        # テーマの設定
        sg.theme('SystemDefaultForReal')

        # ベースのレイアウト
        sg.set_options(element_padding=(0, 0))

        # ヘッダーの列数調整
        if len(self.layouts) % 4 != 0:
            for i in range(4-(len(self.layouts)%4)):
                # self.layouts.append([None, lambda: []])
                NonePage()

        # ヘッダーに⇔ボタンを追加
        header_layouts = [sg.Button(key=f"-COL-PREV0-", button_text=" ", image_data=image_data, image_size=(scroll_button_width, page_title_height), pad=(0, 0), disabled=True)]
        for i in range(len(self.layouts)):
            header_layouts.append(sg.Button(button_text=f"{' ' if self.layouts[i][0] is None else self.layouts[i][0]}", key=f'{i}', image_data=image_data, image_size=(page_title_width, page_title_height), disabled=self.layouts[i][0] is None, pad=(0, 0), tooltip=self.layouts[i][0]))
            if i % 4 == 3:
                header_layouts.append(sg.Button(key=f"-COL-NEXT{i//4}-", button_text=" " if i+1==len(self.layouts) else "→", image_data=image_data, image_size=(scroll_button_width, page_title_height), pad=(0, 0), disabled=(i+1==len(self.layouts))))
                header_layouts.append(sg.Button(key=f"-COL-PREV{(i//4)+1}-", button_text="←", image_data=image_data, image_size=(scroll_button_width, page_title_height), pad=(0, 0)))
        
        del header_layouts[-1]

        window_layout = [
            # [sg.Column([[sg.Button(button_text=f"{layout[0]}", key=f'{i}', image_data=image_data, image_size=(80, 15)) for i, layout in enumerate(self.layouts)]], key="COL-topbar", scrollable=False, size=(window_width + 20, None), pad=(0, 0))],
            [sg.Column([header_layouts], key="COL-topbar", scrollable=False, size=(window_width, 20), pad=(0, 0))],
            [sg.Column((print(layout) is True) or [layout[1]()], key=f'-COL{i}-', visible=(i==0), size=(window_width, 150), pad=(0, 0)) for i, layout in enumerate(self.layouts)],
            [sg.Push(), sg.Button(key="OK", button_text="OK", pad=(2,2)), sg.Button(key="Cancel", button_text="閉じる", pad=(2,2)), sg.Button(key='Shutdown', button_text="終了", pad=(2,2))]
        ]

        # ウィンドウを作成
        self.window = sg.Window('Window Title', window_layout, size=(window_width, window_height), margins=(0,0), finalize=True)

        # self.window["COL-topbar"].Widget.vscrollbar.pack_forget()

        # ウィンドウ表示ループ
        layout_number = 0
        header_number = 0
        while True:

            #
            if self.window_refresh:
                self.window_refresh = False
                break
            
            # event_wait = threading.Thread(target=self.window.read).start()
            # event, values = event_wait.join()
            event, values = self.window.read(timeout=1000, timeout_key='window-read-timeout')
            print(event, values)

            if event == 'window-read-timeout':
                continue

            # OKボタンが押された場合はOKを表示
            if event == 'OK':
                print('OK')
                continue

            # ウィンドウを閉じるかキャンセルボタンが押された場合はループを抜ける
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break

            # レイアウト切り替えイベント
            if event in [str(i) for i in range(len(self.layouts))]:
                print("change layout")
                self.window[f'-COL{layout_number}-'].update(visible=False)
                self.window[f'-COL{event}-'].update(visible=True)
                layout_number = int(event)
                continue

            # ヘッダーの矢印ボタンイベント
            if "-COL-NEXT" in event:
                print(f"NEXT {header_number} -> {header_number+1}")
                self.window[f'-COL-PREV{header_number}-'].update(visible=False)
                self.window[f'{header_number*4+0}'].update(visible=False)
                self.window[f'{header_number*4+1}'].update(visible=False)
                self.window[f'{header_number*4+2}'].update(visible=False)
                self.window[f'{header_number*4+3}'].update(visible=False)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=False)
                header_number += 1
                self.window[f'-COL-PREV{header_number}-'].update(visible=True)
                self.window[f'{header_number*4+0}'].update(visible=True)
                self.window[f'{header_number*4+1}'].update(visible=True)
                self.window[f'{header_number*4+2}'].update(visible=True)
                self.window[f'{header_number*4+3}'].update(visible=True)
                self.window[f'-COL-NEXT{header_number}-'].update(visible=True)
                continue

            if "-COL-PREV" in event:
                print(f"PREV {header_number} -> {header_number-1}")
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
                continue

            # 終了ボタンが押された時はタスクトレイのプロセスも終了してループを抜ける
            if event == 'Shutdown':
                if self.stop_host_process is not None:
                    self.stop_host_process()
                break
        
        # ウィンドウを閉じる
        self.window.close()
        self.window = None


    # WindowManagerを終了する
    def stop(self):
        print("stopping WindowManager")
        self.window_refresh = True
        # Python GILのエラーが出てしまうのでself.window_refreshを使ってフラグを立てる
        # self.window.write_event_value('window-read-timeout', {"force": True})