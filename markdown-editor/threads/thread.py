#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
import helpers


class Thread(QThread):
    sig = pyqtSignal(str)

    def __init__(self, parent):
        super(Thread, self).__init__(parent)

    def run(self):
        helpers.raise_attribute_error(self, 'run')
