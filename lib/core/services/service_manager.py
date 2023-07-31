import threading

from ..service import BaseService

class ServiceManager(BaseService):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.threads = []
        self.stop_callbacks = []

    # サービスを追加
    def add_service(self, service=None):
        if service is None:
            return
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
        for thread in self.threads:
            thread.join()