# utils
setup:
	python3.10 -m venv env
	env/bin/python -m pip install -r requirements.txt

build:
	env/bin/pyinstaller