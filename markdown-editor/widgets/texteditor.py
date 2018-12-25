#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import (
    QPlainTextEdit,
    QSizePolicy,
    QTextDocument,
    QTextCursor,
    QTimer
)


class TextEditor(QPlainTextEdit):
    """docstring for TextEditor."""
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

    @property
    def textContent(self):
        return self.toPlainText()

    @textContent.setter
    def textContent(self, textContent):
        self.setPlainText(textContent)

    @property
    def timeout(self):
        return self.__timer.timeout

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

    def zoomIn(self, range=1):
        range = abs(range)
        super(TextEditor, self).zoomIn(range)
        self.__zoomLevel += range

    def zoomOut(self, range=1):
        range = abs(range)
        super(TextEditor, self).zoomOut(range)
        self.__zoomLevel -= range

    def zoomOriginal(self):
        print(self.__zoomLevel)
        if self.__zoomLevel > 0:
            self.zoomOut(self.__zoomLevel)
        else:
            self.zoomIn(self.__zoomLevel)
