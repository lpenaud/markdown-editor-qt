#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QAction, QIcon, QKeySequence

class Action(QAction):
    """docstring for Action."""
    def __init__(self, label = None, onTriggered = None, keysequence = None, iconName = None, parent = None):
        super(Action, self).__init__(parent)
        self.label = label
        self.triggered.connect(onTriggered)
        self.keysequence = keysequence
        self.iconName = iconName

    @property
    def label(self):
        return self.text()

    @label.setter
    def label(self, label):
        self.setText(label)
        self.setToolTip(label)

    @property
    def iconName(self):
        return self._iconName

    @iconName.setter
    def iconName(self, iconName):
        self.setIcon(QIcon.fromTheme(iconName))
        self._iconName = iconName

    @property
    def keysequence(self):
        return self._keysequence

    @keysequence.setter
    def keysequence(self, keysequence):
        self.setShortcut(QKeySequence(keysequence))
        self._keysequence = keysequence
