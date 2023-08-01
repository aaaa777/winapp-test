import sys
import os

from .utils import FileResolver

class ModLoader:
    @staticmethod
    def init_mods():
        mods_path = os.path.join(FileResolver.get_exe_root_path(), "mods")

        if not os.path.exists(mods_path):
            return

        # モジュールのパスを追加する
        if not mods_path in sys.path:
            sys.path.append(mods_path)

        # モジュールをロードする
        mods = [f.name for f in os.scandir(mods_path) if f.is_dir() and f.name.startswith("mod_")]
        for mod in mods:
            print(f"Loading mod: {mod}")
            __import__(mod)