#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QWidget, QBoxLayout

class Box(QWidget):
    """docstring for BoxLayout."""
    def __init__(self, direction):
        super(Box, self).__init__()
        self._box = QBoxLayout(direction)
        self.setLayout(self._box)

    def addWidget(self, widget, stretch = 0):
        self._box.addWidget(widget, stretch)
