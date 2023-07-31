import threading

class BaseService:
    def __init__(self, disable_thread=False, stop_callback=None):

        if disable_thread:
            self.thread = None
        else:
            self.thread = threading.Thread(target=self.run_thread)
        
        self.stop_callback = stop_callback
        self.stop_callbacks = []

    # サービス終了時に呼び出すコールバックを追加
    def add_stop_callback(self, stop_callback=None):
        if stop_callback is not None:
            self.stop_callbacks.append(stop_callback)

    # 外部から終了させる場合は、このメソッドを呼び出す
    def stop(self):
        for stop_callback in self.stop_callbacks:
            stop_callback()

    # threadingを利用して、別スレッドで実行開始
    def run(self):
        if self.thread is None:
            return
        self.thread.start()
        self.thread.join()

    def run_thread(self):
        pass