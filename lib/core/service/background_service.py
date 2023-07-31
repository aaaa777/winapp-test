from .managed_service import ManagedService

class BackgroundService(ManagedService):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def run_thread(self):
        raise NotImplementedError("run_thread() should be implemented in BackgroundService subclass!")