import sys, os

# This class is used to resolve the absolute path of a file
# when the application is running in a PyInstaller bundle.

# https://stackoverflow.com/questions/41864951/pyinstaller-3-adding-datafiles-with-onefile?rq=3
class FileResolver:

    # ファイルパスを絶対パスで取得する
    # 単一ファイルでexe化した場合は、sys._MEIPASSを使わなければいけません
    @staticmethod
    def resolve_absolute_path(path):
        if getattr(sys, 'frozen', False):
            # if you are running in a |PyInstaller| bundle
            extDataDir = sys._MEIPASS
            extDataDir  = os.path.join(extDataDir, path) 
            #you should use extDataDir as the path to your file Store_Codes.csv file
        else:
            # we are running in a normal Python environment
            extDataDir = os.getcwd()
            extDataDir = os.path.join(extDataDir, path) 
        return extDataDir
    
# バージョンを管理、比較するクラス
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    # バージョンを文字列で取得する
    def get_version_string(self):
        return f"{self.major}.{self.minor}.{self.patch}"
    
    # バージョンを比較する
    # self > other: 1
    # self < other: -1
    # self == other: 0
    def compare(self, other):
        if self.major > other.major:
            return 1
        if self.major < other.major:
            return -1
        if self.minor > other.minor:
            return 1
        if self.minor < other.minor:
            return -1
        if self.patch > other.patch:
            return 1
        if self.patch < other.patch:
            return -1
        return 0

class Consts:

    window_width = 400
    window_height = 200

    # update_interval = 2 * 60 * 60 # 2 hours
    update_interval = 10 # 10 seconds

    mit_license = """Copyright 2023 aaaa777

Permission is hereby granted, free of charge, to 
any person obtaining a copy of this software and 
associated documentation files (the “Software”), 
to deal in the Software without restriction, 
including without limitation the rights to use, 
copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is 
furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission 
notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT 
WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE."""
