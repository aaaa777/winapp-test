import threading

class ServiceManager:
    def __init__(self):
        self.thread = None
        self.threads = []
        self.stop_callbacks = []

    def add_service(self, service=None):
        if service is None:
            return
        self.add_thread(service.thread)
        self.add_stop_callback(service.stop)

    # サービス終了時に呼び出すコールバックを追加
    def add_stop_callback(self, stop_callback=None):
        if stop_callback is not None:
            self.stop_callbacks.append(stop_callback)

    # 待ち合わせるスレッドを追加
    # ここに追加されたスレッドが全て終了すると、run()が終了する
    def add_thread(self, thread):
        if thread is None:
            return
        self.threads.append(thread)

    # def remove_thread(self, thread):
    #     self.threads.remove(thread)

    def stop(self):
        for stop_callback in self.stop_callbacks:
            print(stop_callback)
            stop_callback()

    # ServiceManagerを起動する
    def run(self):
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.start()
        self.thread.join()

    def run_thread(self):
        for thread in self.threads:
            thread.join()