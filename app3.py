from lib.core.services import WindowManager, ServiceManager, TaskTray, UpdateChecker
from lib.core.utils import FileResolver, Consts
from lib.core.page import MainPage, TextPage
from lib.core.version import AppVersion
from lib.core.modloader import ModLoader

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
    # どのサービスよりも最初に初期化すること
    sm = ServiceManager()


    # UpdateCheckerの初期化
    uc = UpdateChecker(
        version_url="http://www.example.com/",
        update_message="アップデートがあります。",
    )


    # WindowManagerの初期化
    wm = WindowManager(
        window_height=Consts.window_height,
        window_width=Consts.window_width,

        # WindowManagerの終了処理にServiceManagerの終了処理を追加
        stop_host_process=sm.stop,
    )

    # WindowManagerにページを追加
    TextPage(title="全般", text="正常に起動しました。"),
    TextPage(title="認証", text="認証済みです。"),
    MainPage(title="メイン"),
    TextPage(title="バージョン", header="バージョン情報", text=f"バージョン: {AppVersion.version.get_version_string()}"),
    TextPage(title="バージョン", header="バージョン情報", text=AppVersion.version.get_version_string()),
    TextPage(title="バージョン", header="バージョン情報", text=AppVersion.version.get_version_string()),
    TextPage(title="ライセンス", header="ライセンス情報", text=Consts.mit_license),
    TextPage(title="ライセンス", header="ライセンス情報", text=Consts.mit_license),


    # TaskTrayの初期化
    tt = TaskTray(

        title="テストアプリ",
        description="テストアプリの説明",
        icon_path=FileResolver.resolve_absolute_path("res/icon.ico"),
        
        # WindowManagerの終了処理にServiceManagerの終了処理を追加
        menu_options={
            '設定': wm.create_window_thread,
            'アップデート': uc.check_update_notification,
            '終了': sm.stop
        },
        default_item="設定",
    )


    # ModLoaderの初期化
    ModLoader.init_mods()


    # ServiceManagerを起動、ブロッキング
    sm.run()

if __name__ == '__main__':
    main()