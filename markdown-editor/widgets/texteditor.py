#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QPlainTextEdit

class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
    def __init__(self, main_window, x, y, width, heigth):
        super(TextEditor, self).__init__(main_window)
        self.insertPlainText('You can write here.\n')
        self.move(x,y)
        self.resize(width,heigth)
        self.canPaste = True
