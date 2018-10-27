#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QTextEdit

class Overview(QTextEdit):
    """docstring for Overview."""
    def __init__(self, parent):
        super(Overview, self).__init__(parent)
        super(Overview, self).setReadOnly(True)
        super(Overview, self).setUndoRedoEnabled(False)

    @property
    def textContent(self):
        return self.toPlainText()

    @property
    def html(self):
        return self.toHtml()

    @html.setter
    def html(self, html):
        self.setHtml(html)

    def setReadOnly(self, ro):
        pass

    def setUndoRedoEnabled(self, enable):
        pass
