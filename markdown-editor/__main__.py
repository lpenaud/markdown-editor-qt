#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
from PyQt5.Qt import QApplication
import helpers

if helpers.is_frozen():
    sys.path.insert(0, str(Path(__file__).parent().parent()))
else:
    sys.path.insert(0, '.')

from markdowneditor import MarkdownEditor

if __name__ == '__main__':
    foption = None
    if len(sys.argv) > 1:
        index = helpers.find_index(sys.argv, '-f')
        if index > -1:
            sys.argv.pop(index)
            try:
                foption = sys.argv[index]
                sys.argv.pop(index)
            except IndexError:
                print('Warning: no file specified after -f option', file=sys.stderr)
    app = QApplication(sys.argv)
    mainWin = MarkdownEditor(foption)
    mainWin.show()
    response = app.exec_()
    sys.exit(response)
