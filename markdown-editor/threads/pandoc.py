#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .thread import Thread
from pandoc import Pandoc

class PandocThread(Thread):
    def __init__(self, parent, input_format, output_format, activateSig, **kwargs):
        super(PandocThread, self).__init__(parent)
        self.pandoc = Pandoc(input_format, output_format, **kwargs)
        self.pathname = kwargs.get('pathname')
        self.intoFile = False
        activateSig.connect(self.start)

    def start(self, text, intoFile=False):
        self.intoFile = intoFile
        super(PandocThread, self).start()

    def run(self):
        self.sig.emit(
            self.pandoc.convert_text(
                self.parent().textEditor.textContent
            )
        )
