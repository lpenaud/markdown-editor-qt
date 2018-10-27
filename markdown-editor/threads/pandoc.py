#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSignal
from .thread import Thread
from pandoc import Pandoc
import helpers

class PandocThread(Pandoc, Thread):

    convertedText = pyqtSignal(str, str)

    def __init__(self, parent, input_format, output_format, activateSig, **kwargs):
        Thread.__init__(self, parent)
        Pandoc.__init__(self, input_format, output_format, **kwargs)
        self.pathname = kwargs.get('pathname')
        self.intoFile = False
        self.text = ''
        activateSig.connect(self.start)

    @property
    def pathname(self):
        return self.__pathname

    @pathname.setter
    def pathname(self, pathname):
        if pathname:
            self.__pathname = helpers.absolute_path(pathname)
        else:
            self.__pathname = None

    def start(self, text, intoFile):
        self.intoFile = intoFile
        self.text = text
        super(PandocThread, self).start()

    def run(self):
        converted_text = self.convert_text(self.text)
        if self.intoFile:
            self.pathname.write_text(converted_text)
        self.convertedText.emit(
            converted_text,
            '' if not(self.intoFile) else str(self.pathname)
        )
        self.text = ''
