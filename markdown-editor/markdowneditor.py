#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.Qt import QApplication, QBoxLayout
from PyQt5 import QtCore
import widgets
import dialogs
import threads
import helpers
import object
from pandoc import Pandoc

class MarkdownEditor(widgets.MainWindow):
    """docstring for MarkdownEditor."""
    def __init__(self):
        super(MarkdownEditor, self).__init__('Markdown Editor', 800, 400)
        tmpfile = helpers.mktemp(suffix = '.html')
        self._box = widgets.Box(QBoxLayout.LeftToRight)
        self._textFileChooser = dialogs.TextFileChooser(self)
        self.pathnameSrc = None

        self.addAction('file-document-new', object.Action('New document', self.triggeredNewDocument, 'Ctrl+N', 'document-new'))
        self.addAction('file-document-open', object.Action('Open document', self.triggeredOpenDocument, 'Ctrl+O', 'document-open'))
        self.addAction('file-document-save', object.Action('Save document', self.triggeredSaveDocument, 'Ctrl+S', 'document-save'))
        self.addAction('file-document-save-as', object.Action('Save document as', self.triggeredSaveAsDocument, 'Ctrl+Shift+S', 'document-save-as'))
        self.addAction('file-export-html', object.Action('Export in html', self.triggeredExport))
        self.addAction('edit-undo', object.Action('Undo', self.triggeredUndo, 'Ctrl+Z', 'edit-undo'))
        self.addAction('edit-redo', object.Action('Redo', self.triggeredRedo, 'Ctrl+Y', 'edit-redo'))
        self.addAction('edit-cut', object.Action('Cut', self.triggeredCut, 'Ctrl+X', 'edit-cut'))
        self.addAction('edit-copy', object.Action('Copy', self.triggeredCopy, 'Ctrl+C', 'edit-copy'))
        self.addAction('edit-paste', object.Action('Paste', self.triggeredPaste, 'Ctrl+V', 'edit-paste'))
        self.addAction('view-refresh', object.Action('Refresh Preview', self.triggeredPreview))

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

        self._menubar = widgets.MenuBar()
        self._menubar.appendMenu('File')
        self._menubar.addActionsToMenu('File', self.findActionsLike('file'))
        self._menubar.insertSeparatorToMenu('File', self.actions['file-document-save'])
        self._menubar.insertSeparatorToMenu('File', self.actions['file-export-html'])
        self._menubar.appendMenu('Edit')
        self._menubar.addActionsToMenu('Edit', self.findActionsLike('edit'))
        self._menubar.insertSeparatorToMenu('Edit', self.actions['edit-cut'])
        self._menubar.appendMenu('View')
        self._menubar.addActionToMenu('View', self.actions['view-refresh'])
        self.setMenuBar(self._menubar)

        self._toolbar = widgets.ToolBar()
        self._toolbar.addActions(self.actions.values())
        self._toolbar.insertSeparator(self.actions['file-export-html'])
        self._toolbar.insertSeparator(self.actions['edit-cut'])
        self._toolbar.insertSeparator(self.actions['edit-undo'])
        self._toolbar.insertSeparator(self.actions['view-refresh'])
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
            self._textFileChooser.setDefaultFilter(0)
            self._textFileChooser.setWindowTitle('Save file')
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
        if self.pathnameSrc:
            self._textFileChooser.setDefaultFilter(1)
            self._textFileChooser.setWindowTitle('Export html')
            if dialogs.isAccepted(self._textFileChooser.exec_()):
                self.pandoc.convert_file(str(self.pathnameSrc), str(self._textFileChooser.pathname))


def main():
    app = QApplication(sys.argv)
    mainWin = MarkdownEditor()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
