#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QMenuBar, QMenu, QIcon, QKeySequence, QAction
from PyQt5.QtGui import QKeySequence


class MenuBar(QMenuBar):
    """docstring for MenuBar."""
    def __init__(self, parent = None):
        super(MenuBar, self).__init__(parent)
        self.menus = []

    def appendMenu(self, title, iconName = None):
        self.menus.append(QMenu(title, self))
        iMenu = len(self.menus) - 1
        if iconName:
            self.menus[iMenu].setIcon(QIcon.fromTheme(iconName))
        self.addMenu(self.menus[iMenu])

    def findIndexMenu(self, title):
        for i in range(0, len(self.menus)):
            if self.menus[i].title() == title:
                return i
        return -1

    def addActionToMenu(self, menuTitle, action):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self.menus[iMenu].addAction(action)

    def addActionsToMenu(self, menuTitle, actions):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self.menus[iMenu].addActions(actions)

    def addSeparatorToMenu(self, menuTitle):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self.menus[iMenu].addSeparator()

    def insertSeparatorToMenu(self, menuTitle, actionBefore):
        iMenu = self.findIndexMenu(menuTitle)
        if iMenu == -1:
            raise ValueError('Unknown menu')
        self.menus[iMenu].insertSeparator(actionBefore)
