init:
	pip install -r requirements.txt

freeze:
	pyinstaller pyinstaller.spec
