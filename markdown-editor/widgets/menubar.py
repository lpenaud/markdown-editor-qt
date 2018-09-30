#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QMenuBar, QMenu, QIcon, QKeySequence, QAction
from PyQt5.QtGui import QKeySequence

class MenuBar(QMenuBar):
    """docstring for MenuBar."""
    def __init__(self, parent = None):
        super(MenuBar, self).__init__(parent)
        self._menus = []
        self._actions = []

    def appendMenu(self, title, iconName = None):
        self._menus.append(QMenu(title, self))
        iMenu = len(self._menus) - 1
        if iconName:
            self._menus[iMenu].setIcon(QIcon.fromTheme(iconName))
        self.addMenu(self._menus[iMenu])

    def findIndexMenu(self, title):
        for i in range(0, len(self._menus)):
            if self._menus[i].title() == title:
                return i
        return -1

    def addNewActionToMenu(self, menuTitle, text, cb, keysequence = None, iconName = None):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self._actions.append(QAction(self))
        iAction = len(self._actions) - 1
        self._actions[iAction].setText(text)
        self._actions[iAction].setToolTip(text)
        self._actions[iAction].triggered.connect(cb)
        if keysequence:
            self._actions[iAction].setShortcut(QKeySequence(keysequence))
        if iconName:
            self._actions[iAction].setIcon(QIcon.fromTheme(iconName))
        self._menus[iMenu].addAction(self._actions[iAction])

    def addActionToMenu(self, menuTitle, action):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self._menus[iMenu].addAction(action)

    def addActionsToMenu(self, menuTitle, actions):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self._menus[iMenu].addActions(actions)

    def addSeparatorToMenu(self, menuTitle):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self._menus[iMenu].addSeparator()

    def insertSeparatorToMenu(self, menuTitle, actionBefore):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self._menus[iMenu].insertSeparator(actionBefore)
