from lib.core.service import ManagedService

from lib.core.services import WindowManager

class SampleModService(ManagedService):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print(WindowManager.init.layouts)