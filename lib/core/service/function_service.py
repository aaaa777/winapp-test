from .base_service import BaseService

class FunctionService(BaseService):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def run(self):
        pass

    def stop(self):
        pass