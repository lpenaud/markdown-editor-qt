#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import widgets
from PyQt5.Qt import QApplication

class MarkdownEditor(widgets.MainWindow):
    """docstring for MarkdownEditor."""
    def __init__(self):
        super(MarkdownEditor, self).__init__('Markdown Editor', 800, 400)
        self._text_edit = widgets.TextEditor(self,0,0,400,400)
        self._text_edit.textChanged.connect(self.onTextChanged)
        self._webview = widgets.WebView(self,401,0,400,400)

    def onTextChanged(self):
        template = '<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>Hello world</title></head><body><pre>{}</pre></body></html>'
        self._webview.html = template.format(self._text_edit.text_content)

def main():
    app = QApplication(sys.argv)
    mainWin = MarkdownEditor()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
