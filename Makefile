all: init icons freeze

icons:
	git clone https://github.com/KDE/oxygen-icons.git icons/oxygen
	git clone https://github.com/stephenc/tango-icon-theme.git icons/tango
	mv icons/tango/index.theme.in icons/tango/index.theme

init:
	pip install -r requirements.txt

freeze:
	pyinstaller pyinstaller.spec
