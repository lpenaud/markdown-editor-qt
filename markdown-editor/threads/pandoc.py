#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .thread import Thread

class PandocThread(Thread):
    def __init__(self, parent, pathname):
        super(PandocThread, self).__init__(parent)
        self.pathname = str(pathname)
        self.sig.connect(parent.cbPandocThread)

    def run(self):
        self.parent().pandoc.convert_text(self.parent().textEditor.textContent, self.pathname)
        self.sig.emit('conversion-end')
