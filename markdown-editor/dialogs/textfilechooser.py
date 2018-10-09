#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QFileDialog
from pathlib import Path
from .helpers import isAccepted, isRejected
import helpers

class TextFileChooser(QFileDialog):
    """docstring for TextFileChooser."""
    def __init__(self, parent):
        super(TextFileChooser, self).__init__(parent)
        self.__filters = ["Markdown file (*.md)", "Html file (*.html)", "All files (*.*)"]
        self.setNameFilters(self.__filters)
        self.selectNameFilter(self.__filters[0])
        self.pathname = Path.home()
        self.mode = 'r'
        self.encoding = 'utf8'

    @property
    def pathname(self):
        return self.__pathname

    @pathname.setter
    def pathname(self, pathname):
        if pathname == None or not(pathname):
            path = Path.home()
        else:
            path = Path.absolute(Path(pathname))
        self.__pathname = path
        if path.is_file():
            path = path.parent
        self.setDirectory(str(path))

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        modes = ('r','w')
        if mode in modes:
            if mode == modes[0]:
                self.setAcceptMode(QFileDialog.AcceptOpen)
            else:
                self.setAcceptMode(QFileDialog.AcceptSave)
            self.__mode = mode
        else:
            raise ValueError('{} is not a available mode'.format(mode))

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding):
        if not(helpers.check_if_encoding_exist(encoding)):
            raise ValueError('{} code is unknown'.format(encoding))
        self.__encoding = encoding

    @property
    def filter(self):
        return self.__filters.copy()

    @filter.setter
    def filter(self, filters):
        self.__filters = filters

    def exec_(self):
        if self.mode == 'w':
            self.selectFile(str(self.pathname.joinpath('New document.{}'.format(self.defaultSuffix()))))
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

    def addFilter(self, filter):
        self.__filters.append(filter)
        self.setNameFilters(self.__filters)
        self.selectNameFilter(self.__filters[0])

    def addFilters(self, filters):
        self.__filters.extend(filters)
        self.setNameFilter(filters)
        self.selectNameFilter(self.__filters[0])

    def setDefaultFilter(self, index):
        self.selectNameFilter(self.__filters[index])
        self.setDefaultSuffix(self.__filters[index].split('(')[1][2:-1])
