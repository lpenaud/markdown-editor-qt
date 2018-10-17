#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QAbstractButton, QCheckBox, pyqtSignal
from .option import Option


class SaveOption(Option):
    """docstring for Save."""

    saveOptionChanged = pyqtSignal(bool)

    def __init__(self, parent, autosaveStatus):
        super(SaveOption, self).__init__(parent)
        self.__autosaveStatus = autosaveStatus

        self.checkBox = QCheckBox(self)
        self.checkBox.setTristate(False)
        self.checkBox.setChecked(self.__autosaveStatus)
        self.checkBox.setText("Autosave")
        self.checkBox.setToolTip("Autosave")
        self.checkBox.stateChanged.connect(self.onCheckBoxStateChanged)
        self.addWidget(self.checkBox)

    def onCheckBoxStateChanged(self, state):
        print(state)
        self.saveOptionChanged.emit(self.checkBox.isChecked())

    def rollback(self):
        self.onCheckBoxStateChanged(self.__autosaveStatus)

    def commit(self):
        self.__autosaveStatus = self.checkBox.isChecked()
