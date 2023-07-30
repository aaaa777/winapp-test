
import argparse
import os
import sys
import time

def setup():
    os.system(f"{os.getcwd()}/env/Scripts/pip install -r requirements.txt")

def build(target, options=""):
    os.system(f"""{os.getcwd()}/env/Scripts/pyinstaller {target} --add-data "res/app.ico;./res/" --add-data "lib/*;./lib/" --clean {options} --noconfirm""")

def run(target):
    os.system(f"""{os.getcwd()}/env/Scripts/python {target} """)


ps = argparse.ArgumentParser(description='win test app build utilities')
ps.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
ps.add_argument('--setup', help='setup.py', action='store_true', default=False)
ps.add_argument('--build', help='build.py', action='store_true', default=False)
ps.add_argument('--run', help='test.py', action='store_true', default=False)
ps.add_argument('--production', dest='production', help='production build', action='store_true', default=False)
ps.add_argument('--development', dest='development', help='development build with console window', action='store_true', default=False)

ns = ps.parse_args(sys.argv[1:])


def main(ns):
    print(ns)
    options = ""

    if ns.production:
        options = "--onefile --noconsole"

    if ns.development:
        options = "--console"

    if ns.production and ns.development:
        print("Error: --production and --development are mutually exclusive")
        return

    if ns.setup:
        setup()
        return
    
    if ns.build:
        build("app3.py", options)
        return
    
    if ns.run:
        run("app3.py")
        return
    



if __name__ == '__main__':
    main(ns)