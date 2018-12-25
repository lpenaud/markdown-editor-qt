#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import (
    QPlainTextEdit,
    QSizePolicy,
    QTextDocument,
    QTextCursor,
    QTimer,
    pyqtSignal
)


class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""

    zoomSignal = pyqtSignal(int)

    @staticmethod
    def getMinZoom():
        return -8

    def __init__(self, parent = None, text = '\n', tabStopDistance = 20):
        super(TextEditor, self).__init__(parent)
        self.insertPlainText(text)
        self.setTabStopDistance(tabStopDistance)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__timer = QTimer(self)
        self.textChanged.connect(self.onTextChanged)
        self.__timer.setSingleShot(True)
        self.htmlFind = '<span style="background-color: turquoise;">{}</span>'
        self.__zoomLevel = 0
        self.__maxZoom = 500
        self.__minZoom = TextEditor.getMinZoom()

    @property
    def textContent(self):
        return self.toPlainText()

    @textContent.setter
    def textContent(self, textContent):
        self.setPlainText(textContent)

    @property
    def timeout(self):
        return self.__timer.timeout

    @property
    def minZoom(self):
        return self.__minZoom

    @minZoom.setter
    def minZoom(self, minZoom):
        err = "minZoom ({}) can't be".format(minZoom)
        if minZoom < TextEditor.getMinZoom():
            err += " inferior to {}"
            raise ValueError(err.format(TextEditor.getMinZoom()))
        if minZoom >= self.maxZoom:
            err += " superior or equal of maxZoom {}"
            raise ValueError(err.format(self.maxZoom))
        self.__minZoom = minZoom

    @property
    def maxZoom(self):
        return self.__maxZoom

    @maxZoom.setter
    def maxZoom(self, maxZoom):
        if maxZoom <= self.minZoom:
            raise ValueError(
                "maxZoom ({}) can't be inferior or equal to minZoom ({})".format(
                    maxZoom,
                    self.minZoom
                )
            )
        self.__maxZoom = maxZoom

    def onTextChanged(self):
        self.__timer.start(300)

    def __find(self, text, cursor, findFlag):
        if not(cursor.isNull()) and not(cursor.atEnd()):
            cursor = self.document().find(text, cursor, findFlag)
            cursor.movePosition(QTextCursor.NextWord, QTextCursor.KeepAnchor, 0)
            cursor.insertHtml(self.htmlFind.format(cursor.selectedText()))
            self.__find(text, cursor, findFlag)

    def find(self, text, findFlag=QTextDocument.FindWholeWords):
        self.textContent = self.textContent
        cursor = QTextCursor(self.document())
        cursor.beginEditBlock()
        self.__find(text, cursor, findFlag)
        cursor.endEditBlock()

    def zoomIn(self, level=1):
        level = abs(level)
        if level + self.__zoomLevel < self.maxZoom:
            super(TextEditor, self).zoomIn(level)
            self.__zoomLevel += level
        self.zoomSignal.emit(self.__zoomLevel)

    def zoomOut(self, level=1):
        level = abs(level)
        if self.__zoomLevel - level > self.minZoom:
            super(TextEditor, self).zoomOut(level)
            self.__zoomLevel -= level
        self.zoomSignal.emit(self.__zoomLevel)

    def zoomOriginal(self):
        if self.__zoomLevel > 0:
            self.zoomOut(self.__zoomLevel)
        else:
            self.zoomIn(self.__zoomLevel)
        self.zoomSignal.emit(self.__zoomLevel)
