import threading

class BaseService:
    def __init__(self, thread_manager=None):
        self.thread_manager = thread_manager
        self.thread = None
        self.stop_callbacks = []

    # 外部から終了させる場合は、このメソッドを呼び出す
    def stop(self):
        for stop_callback in self.stop_callbacks:
            stop_callback()

    # threadingを利用して、別スレッドで実行開始
    def run(self):
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.start()
        self.thread.join()

    def run_thread(self):
        pass