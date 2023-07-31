from datetime import datetime
import requests
import pytz
import threading
from win11toast import toast
from win10toast import ToastNotifier

from ..service import BackgroundService
from ..utils import Version, Consts

class UpdateChecker(BackgroundService):

    def __init__(self, version_url=None, update_message=None, **kwargs):
        super().__init__(**kwargs)
        self.version_url = version_url
        self.update_message = update_message
        self.stop_event = threading.Event()

    def run_thread(self):
        while True:
            date = datetime.now(pytz.timezone('Asia/Tokyo'))
            print(date)

            # self.sleep()は、指定秒数sleepする
            # サービスのstop()が呼ばれた場合は、Trueを返す
            if self.sleep(Consts.update_interval):
                break

    # アップデートがあるかどうかを手動でチェックして、結果を通知する
    def check_update_notification(self):
        pass
        res = toast("アップデートはありませんでした")
        print("toast message", res)

    def check_version(self):
        res = requests.get(self.version_url)

        # version_urlは"major.minor.patch"のバージョンが返る
        return Version("0.0.3")

    # stop()を待機しながら指定秒数sleepする
    # stop()が呼び出された場合は、Trueを返す
    def sleep(self, seconds):
        if self.stop_event.wait(timeout=seconds):
            return True
        return False
        
    def stop(self):
        self.stop_event.set()

