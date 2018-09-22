#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWebKitWidgets import QWebView

class WebView(QWebView):
    """docstring for WebView."""
    def __init__(self, main_window, x, y, width, heigth):
        super(WebView, self).__init__(main_window)
        self.move(x, y)
        self.resize(width, heigth)
        self.setHtml('<!DOCTYPE html><html lang="en" dir="ltr"><head><meta charset="utf-8"><title>Hello world</title></head><body><pre>{}</pre></body></html>'.format('Hello world!'))
