#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QDialog, QTabWidget, QVBoxLayout, QDialogButtonBox
from .themechooser import ThemeChooser

class Preferences(QDialog):
    """docstring for Preferences."""
    def __init__(self, parent = None):
        super(Preferences, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tab = QTabWidget(self)
        self.themeChooser = ThemeChooser(self.tab)
        self.tab.addTab(self.themeChooser, 'Theme chooser')

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.addButton('Ok', QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton('Cancel', QDialogButtonBox.RejectRole)
        self.buttonBox.addButton('Apply', QDialogButtonBox.ApplyRole).clicked.connect(self.applyButtonTriggered)
        self.buttonBox.accepted.connect(self.acceptButtonTriggered)
        self.buttonBox.rejected.connect(self.rejectButtonTriggered)

        self.layout.addWidget(self.tab)
        self.layout.addWidget(self.buttonBox)
        self.setMinimumWidth(self.themeChooser.width())
        self.setMinimumHeight(self.themeChooser.height())

    def acceptButtonTriggered(self):
        self.accept()
        self.applyButtonTriggered()

    def rejectButtonTriggered(self):
        self.reject()

    def applyButtonTriggered(self):
        self.themeChooser.commit()

    def rollback(self):
        self.themeChooser.rollback()

    def exec_(self):
        self.themeChooser.populateComboBox()
        return super(Preferences, self).exec_()
