#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QToolBar
from .menubar import MenuBar
from object import Action


class MainWindow(QMainWindow):
    """docstring for MainWindow."""
    def __init__(self, title, minw, minh):
        super(MainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(minw, minh)
        self.__actions = {}
        self.menubar = MenuBar(self)

    @property
    def menubar(self):
        return self.menuBar()

    @menubar.setter
    def menubar(self, menuBar):
        self.setMenuBar(menuBar)

    def addAction(self, actionName, action=None, **kwargs):
        if action:
            self.__actions[actionName] = action
        else:
            self.__actions[actionName] = Action(self, **kwargs)
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

    def populateMenubar(self, menuName, actionNames):
        categorie = menuName.lower()
        menuTitle = menuName.title()
        self.menubar.addMenu(menuTitle)
        for actionName in actionNames:
            if actionName == 'separator':
                self.menubar.addSeparatorToMenu(menuTitle)
            else:
                self.menubar.addActionToMenu(
                    menuTitle,
                    self.__actions[actionName]
                )
