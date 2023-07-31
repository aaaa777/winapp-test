from .managed_service import ManagedService

class FunctionService(ManagedService):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def run(self):
        pass

    def stop(self):
        pass