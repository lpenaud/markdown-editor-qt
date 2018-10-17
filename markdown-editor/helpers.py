#!/usr/bin/env python
# -*- coding: utf-8 -*-

from encodings.aliases import aliases
from pathlib import Path
import tempfile
import locale
import sys
import os
import platform

def is_frozen():
    return hasattr(sys, 'frozen')

def check_if_encoding_exist(encoding):
    return encoding in aliases.keys() or encoding in aliases.values()

def joinpath(root, *other):
    return Path.joinpath(root, *other)

def joinpath_to_cwd(*other):
    return joinpath(Path(__file__).parent if is_frozen() else Path.cwd(), *other)

def joinpath_to_home(*other):
    return joinpath(Path.home(), *other)

def local_uri_to_path(uri):
    return Path(uri[8:]) if on_windows() else Path(uri[7:]) # len('file://') == 7

def mktemp(suffix = '', prefix=tempfile.template, dir=None):
    return Path(tempfile.mktemp(suffix, prefix, dir))

def get_lang():
    return locale.getdefaultlocale()[0].split('_')[0]

def find_index(iterable, value):
    for i in range(0, len(iterable)):
        if iterable[i] == value:
            return i
    return -1

def get_environ_var(key_name):
    return os.environ[key_name]

def on_windows():
    return platform.system() == 'Windows'

def on_linux():
    return platform.system() == 'Linux'

def on_mac():
    return platform.system() == 'Darwin'

def listing_subdir(str_path):
    p = Path(str_path)
    return [x for x in p.iterdir() if x.is_dir()]

def raise_type_error(var, expected, passing):
    typeExpected = type(expected)
    if typeExpected is tuple or typeExpected is list:
        expected = ','.join(expected)
    raise TypeError('{} must be {} not a {}'.format(
        var,
        expected,
        passing
    ))

def get_name_obj(obj):
    return type(obj).__name__

def raise_attribute_error(obj, name_method):
    raise AttributeError("'{}' object has no attribute '{}'".format(
        get_name_obj(obj),
        name_method
    ))
