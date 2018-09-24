#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QPlainTextEdit
from PyQt5.QtCore import QTimer

class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
    def __init__(self, text = '\n', tabStopDistance = 20):
        super(TextEditor, self).__init__()
        self.insertPlainText(text)
        self.setTabStopDistance(tabStopDistance)
        self._timer = QTimer(self)
        self.textChanged.connect(self.onTextChanged)
        self._timer.setSingleShot(True)

    @property
    def textContent(self):
        return self.toPlainText()

    @textContent.setter
    def textContent(self, textContent):
        self.setPlainText(textContent)

    @property
    def timeout(self):
        return self._timer.timeout

    def onTextChanged(self):
        self._timer.start(300)
