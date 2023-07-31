from .base_service import BaseService

class ManagedService(BaseService):

    manager = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.__class__.manager is None:
            self.__class__.manager.add_service(self)