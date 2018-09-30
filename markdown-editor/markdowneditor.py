#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.Qt import QApplication, QBoxLayout
from PyQt5 import QtCore
import widgets
import dialogs
import threads
import helpers
from pandoc import Pandoc

class MarkdownEditor(widgets.MainWindow):
    """docstring for MarkdownEditor."""
    def __init__(self):
        super(MarkdownEditor, self).__init__('Markdown Editor', 800, 400)
        tmpfile = helpers.mktemp(suffix = '.html')
        self._box = widgets.Box(QBoxLayout.LeftToRight)
        self._textFileChooser = dialogs.TextFileChooser(self)
        self.pathnameSrc = None

        pandocKargs = {
            'template': str(helpers.joinpath_to_cwd('template', 'default.html')),
            'lang': 'en',
            'inline_css': helpers.joinpath_to_cwd('template', 'default.css').read_text(),
            'toc': True,
            'toc_title': True
        }
        self.pandoc = Pandoc('markdown','html5', **pandocKargs)
        self._thread = threads.PandocThread(self, tmpfile)
        self._threadRunning = False

        self._toolbar = widgets.ToolBar()
        self._toolbar.addAction('document-new', 'New document', self.triggeredNewDocument)
        self._toolbar.addAction('document-open', 'Open document', self.triggeredOpenDocument)
        self._toolbar.addAction('document-save', 'Save document', self.triggeredSaveDocument)
        self._toolbar.addAction('document-save-as', 'Save document as', self.triggeredSaveAsDocument)
        self._toolbar.addAction('document-print', 'Export in html', self.triggeredExport)
        self._toolbar.addAction('document-print-preview', 'Preview', self.triggeredPreview)
        self._toolbar.addSeparator()
        self._toolbar.addAction('edit-cut', 'Cut', self.triggeredCut)
        self._toolbar.addAction('edit-copy', 'Copy', self.triggeredCopy)
        self._toolbar.addAction('edit-paste', 'Paste', self.triggeredPaste)
        self._toolbar.addSeparator()
        self._toolbar.addAction('edit-undo', 'Undo', self.triggeredUndo)
        self._toolbar.addAction('edit-redo', 'Redo', self.triggeredRedo)
        self.addToolBar(self._toolbar)

        self.textEditor = widgets.TextEditor(helpers.joinpath_to_cwd('example', 'example.md').read_text())
        self.textEditor.timeout.connect(self.triggeredTextTimeout)

        self.webview = widgets.WebView()
        self.triggeredPreview()
        self.webview.url = tmpfile.as_uri()

        self._box.addWidget(self.textEditor)
        self._box.addWidget(self.webview)

        self.setCentralWidget(self._box)

    def saveDocument(self, forceAs = False):
        writable = False
        self._textFileChooser.mode = 'w'

        if not(self.textEditor.textContent.endswith('\n')):
            self.textEditor.appendPlainText('')

        if not(self.pathnameSrc) or forceAs:
            if dialogs.isAccepted(self._textFileChooser.exec_()):
                self.pathnameSrc = self._textFileChooser.pathname
                writable = True
        else:
            writable = True

        if writable:
            self.pathnameSrc.write_text(self.textEditor.textContent)

    def openDocument(self):
        self._textFileChooser.mode = 'r'
        response = self._textFileChooser.exec_()
        if dialogs.isAccepted(response):
            self.textEditor.textContent = self._textFileChooser.readText()
            self.pathnameSrc = self._textFileChooser.pathname

    def triggeredTextTimeout(self):
        self.triggeredPreview()

    def triggeredPaste(self):
        self.textEditor.paste()

    def triggeredCopy(self):
        self.textEditor.copy()

    def triggeredCut(self):
        self.textEditor.cut()

    def triggeredUndo(self):
        self.textEditor.undo()

    def triggeredRedo(self):
        self.textEditor.redo()

    def triggeredNewDocument(self):
        self.textEditor.clear()
        self.pathnameSrc = None

    def triggeredOpenDocument(self):
        self.openDocument()

    def triggeredSaveAsDocument(self):
        self.saveDocument(forceAs = True)

    def triggeredSaveDocument(self):
        self.saveDocument()

    def triggeredPreview(self):
        self._thread.start()

    def cbPandocThread(self):
        self.webview.reload()

    def triggeredExport(self):
        self.saveDocument()
        if dialogs.isAccepted(self._textFileChooser.exec_()):
            self.pandoc.convert_file(str(self.pathnameSrc), str(self._textFileChooser.pathname))


def main():
    app = QApplication(sys.argv)
    mainWin = MarkdownEditor()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
