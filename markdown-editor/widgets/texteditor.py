#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QPlainTextEdit, QSizePolicy
from PyQt5.QtCore import QTimer


class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
    def __init__(self, parent = None, text = '\n', tabStopDistance = 20):
        super(TextEditor, self).__init__(parent)
        self.insertPlainText(text)
        self.setTabStopDistance(tabStopDistance)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__timer = QTimer(self)
        self.textChanged.connect(self.onTextChanged)
        self.__timer.setSingleShot(True)

    @property
    def textContent(self):
        return self.toPlainText()

    @textContent.setter
    def textContent(self, textContent):
        self.setPlainText(textContent)

    @property
    def timeout(self):
        return self.__timer.timeout

    def onTextChanged(self):
        self.__timer.start(300)
