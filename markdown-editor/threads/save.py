#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from PyQt5.Qt import pyqtSignal
from .thread import Thread
import helpers


class SaveThread(Thread):

    writed = pyqtSignal(int)

    def __init__(self, parent):
        super(SaveThread, self).__init__(parent)
        self.__p = None
        self.__content = None
        self.__encoding = 'utf_8'
        self.__error = None

    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, p):
        print(p)
        p = Path(p).absolute()
        if p.is_dir():
            raise IsADirectoryError()
        self.__p = p

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding):
        if helpers.check_if_encoding_exist(encoding):
            raise UnicodeError()
        self.__encoding = encoding

    @property
    def error(self):
        return self.__error

    def run(self):
        try:
            self.p.write_text(self.content, encoding=self.encoding)
        except Exception as e:
            self.__error = e
            self.writed.emit(-1)
            return None
        self.__error = None
        self.writed.emit(len(self.content))
