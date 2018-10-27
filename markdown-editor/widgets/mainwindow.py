#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """docstring for MainWindow."""
    def __init__(self, title, minw, minh):
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(minw, minh)
        self.actions = {}

    def addAction(self, actionName, action):
        self.actions[actionName] = action
        super(MainWindow, self).addAction(self.actions[actionName])

    def addActions(self, actions):
        for name, action in actions.items():
            self.addAction(name, action)

    def findActionsLike(self, like):
        result = []
        for key, value in self.actions.items():
            if like in key:
                result.append(value)
        return result
