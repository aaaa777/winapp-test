from .base_service import BaseService

class ManagedService(BaseService):

    # ServiceManager初期化時にセットされる
    manager = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # サービス初期化時にServiceManagerに登録する
        if not self.__class__.manager is None:
            self.__class__.manager.add_service(self)