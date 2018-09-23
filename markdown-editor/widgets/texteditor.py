#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QPlainTextEdit

class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
    def __init__(self):
        super(TextEditor, self).__init__()
        self.insertPlainText('You can write here.\n')

    @property
    def textContent(self):
        return self.toPlainText()

    @textContent.setter
    def textContent(self, textContent):
        self.setPlainText(textContent)
