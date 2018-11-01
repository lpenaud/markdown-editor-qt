#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QMenuBar, QMenu, QIcon, QKeySequence, QAction
from PyQt5.QtGui import QKeySequence


class MenuBar(QMenuBar):
    """docstring for MenuBar."""

    def addMenu(self, title):
        menu = super(MenuBar, self).addMenu(title)
        menu.setWindowTitle(title)

    def findMenu(self, title):
        for menu in self.findChildren(QMenu):
            if menu.windowTitle() == title:
                return menu

    def addActionToMenu(self, menuTitle, action):
        self.findMenu(menuTitle).addAction(action)

    def addActionsToMenu(self, menuTitle, actions):
        self.findMenu(menuTitle).addActions(actions)

    def addSeparatorToMenu(self, menuTitle):
        self.findMenu(menuTitle).addSeparator()

    def insertSeparatorToMenu(self, menuTitle, actionBefore=None):
        self.findMenu(menuTitle).insertSeparator(actionBefore)

    def addSeparatorToMenu(self, menuTitle):
        self.findMenu(menuTitle).addSeparator()
