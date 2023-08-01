from .managed_page import ManagedPage

class NonePage(ManagedPage):
    def __init__(self):
        super().__init__(title=None)

    def layout(self):
        return []