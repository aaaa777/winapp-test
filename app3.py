
from lib.core.tasktray import TaskTray
from lib.core.window.manager import WindowManager
from lib.core.utils import FileResolver

import sys

def main():

    wm = WindowManager()

    print("Start TaskTray")
    
    tt = TaskTray(
        icon_path=FileResolver.resolve_absolute_path("res/app.ico"),
        title="My System Tray Icon",
        description="My System Tray Icon",
        default_item="Launch"
    )

    tt.menu_options={
        'Show': lambda: print("Show"),
        'Test': lambda: print("Test"),
        'Launch': lambda: wm.start(stop_callback=tt.stop),
        'Quit': tt.stop
    }

    tt.start()
    
    tt.wait()
    print("Quit TaskTray")

if __name__ == '__main__':
    main()