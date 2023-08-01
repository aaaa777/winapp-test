from .base_page import BasePage

class ManagedPage(BasePage):

    # WindowManager初期化時に設定される
    manager = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ページ初期化時にWindowManagerに登録する
        if not self.__class__.manager is None:
            self.__class__.manager.add_page(self)
        
