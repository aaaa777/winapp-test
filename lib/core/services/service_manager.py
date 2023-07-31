import threading

from ..service import BackgroundService

class ServiceManager(BackgroundService):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.threads = []
        self.services = []

    # サービスを追加
    def add_service(self, service=None):
        if service is None:
            return
        self.services.append(service)
        self.add_thread(service.thread)
        self.add_stop_callback(service.stop)

    # 待ち合わせるスレッドを追加
    # ここに追加されたスレッドが全て終了すると、run()が終了する
    def add_thread(self, thread=None):
        if thread is None:
            return
        self.threads.append(thread)

    # ServiceManagerをThreadで起動するメソッド
    # self.threadsに追加されたスレッドが全て終了すると、run()が終了する
    def run_thread(self):
        threads = [threading.Thread(target=service.run) for service in self.services]
        for thread in threads:
            thread.start()

        # バックグラウンドのサービスが全て終了するまで待機
        for thread in threads:
            print(thread)
            thread.join()