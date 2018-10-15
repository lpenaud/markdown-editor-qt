#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .thread import Thread

class SaveThread(Thread):
    def __init__(self, parent):
        super(SaveThread, self).__init__(parent)

    def run(self):
        if self.parent().pathnameSrc:
            self.parent().saveDocument()
            self.sig.emit('save-document')
