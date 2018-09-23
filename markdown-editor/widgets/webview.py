#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    """docstring for WebView."""
    def __init__(self, main_window, x, y, width, heigth):
        super(WebView, self).__init__(main_window)
        self.move(x, y)
        self.resize(width, heigth)
        self._html = ''

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, html):
        self._html = html
        self.setHtml(html)
