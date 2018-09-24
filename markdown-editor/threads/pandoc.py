#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore

class PandocThread(QtCore.QThread):
    sig = QtCore.pyqtSignal(str)
    def __init__(self, parent, pathname):
        super(PandocThread, self).__init__(parent)
        self.parent = parent
        self.sig.connect(parent.cbPandocThread)
        self.pathname = str(pathname)

    def run(self):
        self.parent.pandoc.convert_text(self.parent.textEditor.textContent, self.pathname)
        self.sig.emit('conversion-end')
