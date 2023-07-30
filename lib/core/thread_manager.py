import threading

class ThreadManager:
    def __init__(self, base_thread=None):
        self.thread = None
        self.threads = []
        self.base_thread = base_thread
        self.stop_callbacks = []

    def add_stop_callback(self, stop_callback=None):
        if stop_callback is not None:
            self.stop_callbacks.append(stop_callback)

    def add_thread(self, thread):
        self.threads.append(thread)

    # def remove_thread(self, thread):
    #     self.threads.remove(thread)

    def stop(self):
        for stop_callback in self.stop_callbacks:
            print(stop_callback)
            stop_callback()

    def run(self):
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.start()
        self.thread.join()

    def run_thread(self):
        for thread in self.threads:
            thread.join()