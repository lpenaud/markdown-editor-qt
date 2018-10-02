#!/usr/bin/env python
# -*- coding: utf-8 -*-

from encodings.aliases import aliases
from pathlib import Path
import tempfile
import locale
import sys

def check_if_encoding_exist(encoding):
    return encoding in aliases.keys() or encoding in aliases.values()

def joinpath(root, *other):
    return Path.joinpath(root, *other)

def joinpath_to_cwd(*other):
    return joinpath(Path.cwd(), *other)

def joinpath_to_home(*other):
    return joinpath(Path.home(), *other)

def local_uri_to_path(uri):
    return Path(uri[8:]) if sys.platform == 'win32' else Path(uri[7:]) # len('file://') == 7

def mktemp(suffix = '', prefix=tempfile.template, dir=None):
    return Path(tempfile.mktemp(suffix, prefix, dir))

def get_lang():
    return locale.getdefaultlocale()[0].split('_')[0]

def find_index(iterable, value):
    for i in range(0, len(iterable)):
        if iterable[i] == value:
            return i
    return -1
