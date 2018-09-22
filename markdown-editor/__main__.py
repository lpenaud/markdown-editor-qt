
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path

if hasattr(sys, 'frozen'):
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))
else:
    sys.path.insert(0, '.')

import markdowneditor

if __name__ == '__main__':
    markdowneditor.main()
