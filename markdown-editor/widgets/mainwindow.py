#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """docstring for MainWindow."""
    def __init__(self, title, minw, minh):
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(minw, minh)
        self.__actions = {}

    def addAction(self, actionName, action):
        self.__actions[actionName] = action
        super(MainWindow, self).addAction(self.__actions[actionName])

    def addActions(self, actions):
        for name, action in actions.items():
            self.addAction(name, action)

    def getAction(self, key, d=None):
        return self.__actions.get(key, d)

    def findActionsLike(self, like):
        result = []
        for key in self.__actions.keys():
            if like in key:
                result.append(self.getAction(key))
        return result
