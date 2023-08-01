import threading

from ..service import BackgroundService
from ..service import ManagedService

class ServiceManager(BackgroundService):

    managed_services = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.threads = []
        self.services = []
        ManagedService.manager = self

    # サービスを追加
    def add_service(self, service=None):
        if service is None:
            return
        
        print("Adding service: {}".format(service))
        self.services.append(service)
        self.add_stop_callback(service.stop)


    # ServiceManagerをThreadで起動するメソッド
    # self.threadsに追加されたスレッドが全て終了すると、run()が終了する
    def run_thread(self):

        # バックグラウンドのサービスを起動
        threads = [threading.Thread(target=service.run) for service in self.services]
        for thread in threads:
            thread.start()

        # バックグラウンドのサービスが全て終了するまで待機
        for thread in threads:
            print(thread)
            thread.join()