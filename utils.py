
import argparse
import os
import sys
import time

def setup():
    os.system(f"{os.getcwd()}/env/Scripts/pip install -r requirements.txt")

def build(target, options=""):
    os.system(f"""{os.getcwd()}/env/Scripts/pyinstaller {target} --icon "res/tficon2.ico" --add-data "res/*;./res/" --add-data "lib/*;./lib/" --clean {options} --noconfirm""")

def sign(target):
    os.system(f"""openssl pkcs12 -export -inkey cert/code.key -in cert/code.crt -out code.pfx""" )
    os.system(f"""signtool sign /f cert/code.pfx /t http://timestamp.digicert.com /fd SHA256 /p exampleexampleexample dist/app3.exe""" )

def run(target):
    os.system(f"""{os.getcwd()}/env/Scripts/python {target} """)

def version_up(major, minor, patch):

    # lib/core/version.pyを読み込み
    with open("lib/core/version.py", "r") as f:
        lines = f.readlines()
        version_major = int(lines[3].split("=")[1].strip())
        version_minor = int(lines[4].split("=")[1].strip())
        version_patch = int(lines[5].split("=")[1].strip())

    new_version_major = version_major + major
    new_version_minor = 0 if major != 0 else version_minor + minor
    new_version_patch = 0 if major != 0 or minor != 0 else version_patch + patch

    # lib/core/version.pyを更新
    with open("lib/core/version.py", "w") as f:
        f.write(
            f"""from .utils import Version

class AppVersion(Version):
    version_major = {new_version_major}
    version_minor = {new_version_minor}
    version_patch = {new_version_patch}

    singleton = Version(version_major, version_minor, version_patch)"""
        )
    
    os.system(f"""git add lib/core/version.py""")
    os.system(f"""git commit -m "version up v{new_version_major}.{new_version_minor}.{new_version_patch}" """)
    os.system(f"""git push""")
    os.system(f"""git tag -a v{new_version_major}.{new_version_minor}.{new_version_patch} -m "version up v{new_version_major}.{new_version_minor}.{new_version_patch}" """)
    os.system(f"""git push --tags""")
        
def patch_up():
    version_up(0, 0, 1)

def minor_up():
    version_up(0, 1, 0)

def major_up():
    version_up(1, 0, 0)


ps = argparse.ArgumentParser(description='win test app build utilities')
ps.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
ps.add_argument('--setup', help='setup.py', action='store_true', default=False)
ps.add_argument('--build', help='build.py', action='store_true', default=False)

ps.add_argument('--run', help='test.py', action='store_true', default=False)

ps.add_argument('--production', dest='production', help='production build', action='store_true', default=False)
ps.add_argument('--development', dest='development', help='development build with console window', action='store_true', default=False)

ps.add_argument('--bump', help='version up', action='store_true', default=False)
ps.add_argument('--patch', help='patch up', action='store_true', default=False)
ps.add_argument('--minor', help='minor up', action='store_true', default=False)
ps.add_argument('--major', help='major up', action='store_true', default=False)


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
    
    if ns.bump:
        if ns.major:
            major_up()
            return
        if ns.minor:
            minor_up()
            return
        if ns.patch:
            patch_up()
            return
        print("Error: --bump requires --major, --minor or --patch")


if __name__ == '__main__':
    main(ns)