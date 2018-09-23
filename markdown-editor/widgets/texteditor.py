#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QPlainTextEdit

class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
    def __init__(self):
        super(TextEditor, self).__init__()
        self.insertPlainText('You can write here.\n')

    @property
    def text_content(self):
        return self.toPlainText()

    @text_content.setter
    def text_content(self, text_content):
        self.setPlainText(text_content)
