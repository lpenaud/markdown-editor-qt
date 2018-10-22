#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QMessageBox


class MessageBox(QMessageBox):
    """docstring for MessageBox."""
    def __init__(self, parent):
        super(MessageBox, self).__init__(parent)

    @staticmethod
    def documentIsNotSave(parent):
        msgBox = QMessageBox(parent)
        msgBox.setWindowTitle('The document has been modified')
        msgBox.setText('The document has been modified')
        msgBox.setInformativeText('Do you want to save your change?')
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setIcon(QMessageBox.Warning)
        return msgBox.exec_()

    @staticmethod
    def isSaveClicked(dialogCode):
        return dialogCode == QMessageBox.Save

    @staticmethod
    def isDiscardClicked(dialogCode):
        return dialogCode == QMessageBox.Discard

    @staticmethod
    def isCancelClicked(dialogCode):
        return dialogCode == QMessageBox.Cancel
