#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebView(QWebEngineView):
    """docstring for WebView."""
    def __init__(self):
        super(WebView, self).__init__()
        self.__html = ''

    @property
    def html(self):
        return self.__html

    @html.setter
    def html(self, html):
        self.__html = html
        self.setHtml(html)

    @property
    def url(self):
        return super(WebView, self).url().toString()

    @url.setter
    def url(self, url):
        self.setUrl(QUrl(url))
