
from lib.core.tasktray import TaskTray
from lib.core.window.window_manager import WindowManager
from lib.core.utils import FileResolver, Consts
from lib.core.services import ServiceManager
from lib.core.page import MainPage
from lib.core.page import TextPage

import sys
from tendo import singleton

def main():
    # 二重起動防止
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit(0)

    # ServiceManagerの初期化
    sm = ServiceManager()

    # WindowManagerの初期化
    wm = WindowManager(
        stop_callback=sm.stop
    )

    # WindowManagerにページを追加
    pages = [
        TextPage("全般", None, "正常に起動しました。"),
        TextPage("認証", None, "認証済みです。"),
        MainPage("メイン"),
        TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
        TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
        TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
        TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
        TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
        TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
        TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
        TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
        # TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
    ]
    for page in pages:
        wm.add_page(page)

    print("Start Program")
    
    # TaskTrayの初期化
    tt = TaskTray(
        icon_path=FileResolver.resolve_absolute_path("res/icon.ico"),
        title="テストアプリ",
        description="テストアプリの説明",
        default_item="設定"
    )

    # WindowManagerの終了処理にThreadManagerの終了処理を追加

    tt.menu_options={
        '設定': lambda: wm.create_window(),
        '終了': sm.stop
    }

    # 停止処理をThreadManagerに登録
    sm.add_stop_callback(tt.stop)
    sm.add_stop_callback(wm.stop)

    sm.add_thread(tt.start())
    sm.run()

if __name__ == '__main__':
    main()