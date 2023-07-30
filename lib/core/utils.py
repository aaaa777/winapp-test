import sys, os

# This class is used to resolve the absolute path of a file
# when the application is running in a PyInstaller bundle.

# https://stackoverflow.com/questions/41864951/pyinstaller-3-adding-datafiles-with-onefile?rq=3
class FileResolver:
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
