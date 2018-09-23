#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QFileDialog
from pathlib import Path
from .utils import isAccepted, isRejected
import utils

class TextFileChooser(QFileDialog):
    """docstring for TextFileChooser."""
    def __init__(self, parent):
        super(TextFileChooser, self).__init__(parent)
        filter = ["Text file (*.md *.markdown *.rst *.txt)", "All files (*.*)"]
        self.setNameFilters(filter)
        self.selectNameFilter(filter[0])
        self.pathname = Path.home()
        self.mode = 'r'
        self.encoding = 'utf_8'

    @property
    def pathname(self):
        return self._pathname

    @pathname.setter
    def pathname(self, pathname):
        if pathname == None or not(pathname):
            path = Path.home()
        else:
            path = Path.absolute(Path(pathname))
        self._pathname = path
        if path.is_file():
            path = path.parent
        self.setDirectory(str(path))

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        modes = ('r','w')
        if mode in modes:
            if mode == modes[0]:
                self.setAcceptMode(QFileDialog.AcceptOpen)
            else:
                self.setAcceptMode(QFileDialog.AcceptSave)
            self._mode = mode
        else:
            raise ValueError('{} is not a available mode'.format(mode))

    @property
    def encoding(self):
        return self._encoding

    @encoding.setter
    def encoding(self, code):
        if not(code in utils.codes):
            raise ValueError('{} code is unknown'.format(code))
        self._encoding = code

    def exec_(self):
        response = super(TextFileChooser, self).exec_()
        if isAccepted(response):
            self.pathname = self.selectedFiles()[0]
        elif isRejected(response):
            self.pathname = None
        return response

    def writeText(self, text):
        if self.mode == 'w':
            return self.pathname.write_text(text, encoding=self.encoding)
        return 0

    def readText(self):
        return self.pathname.read_text(encoding=self.encoding)
