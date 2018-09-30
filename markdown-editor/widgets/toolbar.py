#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QToolBar, QIcon, QAction

class ToolBar(QToolBar):
    """docstring for ToolBar."""
    def __init__(self):
        super(ToolBar, self).__init__()
        self._actions = []

    def addAction(self, text, cb, iconName = None):
        self._actions.append(QAction())
        index = len(self._actions) - 1
        self._actions[index].setText(text)
        self._actions[index].setToolTip(text)
        self._actions[index].triggered.connect(cb)
        if iconName:
            self._actions[index].setIcon(QIcon.fromTheme(iconName))
        super(ToolBar, self).addAction(self._actions[index])
