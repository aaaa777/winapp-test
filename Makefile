# utils
setup:
	python3.10 -m venv env
	env/bin/python -m pip install -r requirements.txt

build:
	env/bin/pyinstaller app.py --name "app_development"
	env/bin/pyinstaller app.py --noconsole --name "app_production"

build2:
	env/bin/pyinstaller tray.py --add-data "res/app.ico;." --add-data "lib/*;./lib/" --clean --name "tray_development"

build2-win:
	env\Scripts\pyinstaller tray.py --add-data "res/app.ico;." --add-data "lib/*;./lib/" --clean --name "tray_development"