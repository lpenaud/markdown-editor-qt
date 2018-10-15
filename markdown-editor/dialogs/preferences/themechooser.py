#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QWidget, QIcon, QComboBox, QLabel, QVBoxLayout, pyqtSignal
import helpers


class ThemeChooser(QWidget):
    """docstring for ThemeChooser."""

    themeChanged = pyqtSignal(str)

    def __init__(self, parent):
        super(ThemeChooser, self).__init__(parent)
        self.currentIconTheme = QIcon.themeName()
        self.label = QLabel(self)
        self.comboBox = QComboBox(self)
        self.setLayout(QVBoxLayout(self))

        self.label.setText('Available themes :')

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.comboBox)
        self.comboBox.currentTextChanged.connect(self.onThemeChanged)
        self.populateComboBox()

    def populateComboBox(self):
        self.comboBox.clear()
        for path in QIcon.themeSearchPaths():
            for subdir in helpers.listing_subdir(path):
                if subdir.name != self.currentIconTheme:
                    self.comboBox.addItem(subdir.name)
        self.comboBox.insertItem(0, self.currentIconTheme)
        self.comboBox.setCurrentIndex(0)

    def onThemeChanged(self, themeName):
        QIcon.setThemeName(themeName)
        self.themeChanged.emit(themeName)

    def rollback(self):
        self.onThemeChanged(self.currentIconTheme)

    def commit(self):
        self.currentIconTheme = QIcon.themeName()
