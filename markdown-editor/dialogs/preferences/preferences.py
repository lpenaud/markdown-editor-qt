#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QDialog, QTabWidget, QVBoxLayout, QDialogButtonBox
from .themechooser import ThemeChooser
from .saveoption import SaveOption


class Preferences(QDialog):
    """docstring for Preferences."""

    def __init__(self, parent):
        super(Preferences, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tab = QTabWidget(self)
        self.themeChooser = ThemeChooser(self.tab)
        self.tab.addTab(self.themeChooser, 'Theme')

        self.saveOption = SaveOption(self.tab, self.parent().saveThreading)
        self.tab.addTab(self.saveOption, 'Save')
        self.layout.addWidget(self.tab)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.addButton('Ok', QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton('Cancel', QDialogButtonBox.RejectRole)
        self.buttonBox.addButton('Apply', QDialogButtonBox.ApplyRole).clicked.connect(self.commit)
        self.buttonBox.accepted.connect(self.acceptButtonTriggered)
        self.buttonBox.rejected.connect(self.rejectButtonTriggered)
        self.layout.addWidget(self.buttonBox)

        self.setMinimumWidth(self.tab.widget(0).width())
        self.setMinimumHeight(self.tab.widget(0).height())

    def acceptButtonTriggered(self):
        self.accept()

    def rejectButtonTriggered(self):
        self.reject()

    def commit(self):
        for i in range(0, self.tab.count()):
            self.tab.widget(i).commit()

    def rollback(self):
        for i in range(0, self.tab.count()):
            self.tab.widget(i).rollback()
