#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.Qt import QToolBar, QIcon, QAction

class ToolBar(QToolBar):
    """docstring for ToolBar."""
    def __init__(self):
        super(ToolBar, self).__init__()
        self._items = []

    def addAction(self, icon_name, text, cb):
        self._items.append({
            'icon': QIcon.fromTheme(icon_name),
            'action': QAction()
        })
        item = self._items[len(self._items) - 1]
        item['action'].setIcon(item['icon'])
        item['action'].setText(text)
        item['action'].setToolTip(text)
        item['action'].triggered.connect(cb)
        super(ToolBar, self).addAction(item['action'])
