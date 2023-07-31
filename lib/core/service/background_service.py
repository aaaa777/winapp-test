from .base_service import BaseService

class BackgroundService(BaseService):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def run_thread(self):
        raise NotImplementedError("run_thread() should be implemented in BackgroundService subclass!")