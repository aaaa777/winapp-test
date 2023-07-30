
from lib.core.tasktray import TaskTray
from lib.core.window.window_manager import WindowManager
from lib.core.utils import FileResolver, Consts
from lib.core.thread_manager import ThreadManager
from lib.core.window.mainpage import MainPage
from lib.core.window.textpage import TextPage


import sys
from tendo import singleton

def main():
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit(0)

    # ThreadManagerの初期化
    tm = ThreadManager()

    # WindowManagerの初期化
    wm = WindowManager(
        stop_callback=tm.stop
    )

    # WindowManagerにページを追加
    pages = [
        TextPage("全般", None, "正常に起動しました。"),
        TextPage("認証", None, "認証済みです。"),
        MainPage("メイン"),
        TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
        TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
    ]
    for page in pages:
        wm.add_page(page)

    print("Start Program")
    
    # TaskTrayの初期化
    tt = TaskTray(
        icon_path=FileResolver.resolve_absolute_path("res/app.ico"),
        title="テストアプリ",
        description="テストアプリの説明",
        default_item="設定"
    )

    # WindowManagerの終了処理にThreadManagerの終了処理を追加

    tt.menu_options={
        '設定': lambda: wm.create_window(),
        '終了': tm.stop
    }

    # 停止処理をThreadManagerに登録
    tm.add_stop_callback(tt.stop)
    tm.add_stop_callback(wm.stop)

    tm.add_thread(tt.start())
    tm.run()

if __name__ == '__main__':
    main()