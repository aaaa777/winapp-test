import threading
from pystray import Icon,Menu,MenuItem
from PIL import Image
from ..service import BackgroundService

class TaskTray(BackgroundService):

    def __init__(self, icon_path, menu_options={}, title="", description="", default_item=None, **kwargs):
        super().__init__(**kwargs)
        self.icon_path = icon_path
        self.menu_options = menu_options
        self.title = title
        self.description = description
        self.default_item = default_item
        self.icon = None


    # タスクトレイのスレッド化
    def run_thread(self):
        try:
            item=[]

            # クリック時の動作を設定
            for option,callback in self.menu_options.items():
                item.append( MenuItem(option, callback, default=(option==self.default_item) ) )
                
            # メニューを作成
            menu = Menu(*item)

            image = Image.open(self.icon_path)
            self.icon = Icon(
                self.title,
                image,
                self.description,
                menu
            )

            # タスクトレイ常駐
            self.icon.run()
        finally:
            self.stop()

        
    def stop(self):
        if self.icon != 0:
            self.icon.stop()
