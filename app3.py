from lib.core.services import WindowManager, ServiceManager, TaskTray
from lib.core.utils import FileResolver, Consts
from lib.core.page import MainPage, TextPage

import sys
from tendo import singleton

def main():
    print("Start Program")

    # 二重起動防止
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit(0)

    # ServiceManagerの初期化
    sm = ServiceManager()



    # WindowManagerの初期化
    wm = WindowManager(

        # WindowManagerの終了処理にServiceManagerの終了処理を追加
        stop_callback=sm.stop,
    
        # WindowManagerにページを追加
        pages=[
            TextPage("全般", None, "正常に起動しました。"),
            TextPage("認証", None, "認証済みです。"),
            MainPage("メイン"),
            TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
            TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
            TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
            TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
            TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
            TextPage("バージョン", "バージョン情報", "0.0.3 (2023/07/31)"),
            TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
            TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
            # TextPage("ライセンス", "ライセンス情報", Consts.mit_license),
        ],
    )

    # TaskTrayの初期化
    tt = TaskTray(

        title="テストアプリ",
        description="テストアプリの説明",
        icon_path=FileResolver.resolve_absolute_path("res/icon.ico"),
        
        # WindowManagerの終了処理にServiceManagerの終了処理を追加
        menu_options={
            '設定': lambda: wm.create_window_thread(),
            '終了': sm.stop
        },
        default_item="設定",
    )


    # 停止処理をServiceManagerに登録
    sm.add_service(wm)
    sm.add_service(tt)

    # ServiceManagerを起動、ブロッキング
    sm.run()

if __name__ == '__main__':
    main()