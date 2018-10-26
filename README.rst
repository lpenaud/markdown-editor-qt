##################
Markdown Editor
##################

A markdown editor written in Python3.7 with Qt5 and pandoc2

**Advices :**

- Create a virtual environments with ``python -m venv <name of venv>``
- Activate your virtual environment :
    - On GNU/Linux ``source <name of venv>/bin/activate``
    - On Windows ``<name of venv>/Scripts/activate.bat``
- Install all dependencies : ``make``
- To launch : ``python markdown-editor``
- To freeze : ``pyinstaller pyinstaller.spec``
- To launch the frozen application : ``dist/Markdown-Editor/Markdown-Editor``

*****************
TODO
*****************

- Add "about" window
- Add thread to save file
- Add pandoc to preferences window

*****************
License
*****************

This project is licensed under the GPL-3.0 license.
See the `LICENSE <LICENSE>`_ file for more info.
