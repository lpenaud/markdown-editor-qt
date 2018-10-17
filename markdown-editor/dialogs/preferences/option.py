#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QWidget, QVBoxLayout
import helpers


class Option(QWidget):
    """docstring for Option."""

    def __init__(self, parent):
        super(Option, self).__init__(parent)
        self.setLayout(QVBoxLayout(self))

    def addWidget(self, widget):
        self.layout().addWidget(widget)

    def addWidgets(self, widgets):
        for widget in widget:
            self.addWidget(widget)

    def rollback(self):
        helpers.raise_attribute_error(self, 'rollback')

    def commit(self):
        helpers.raise_attribute_error(self, 'commit')
