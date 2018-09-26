#!/usr/bin/env python
# -*- coding: utf-8 -*-

from encodings.aliases import aliases
from pathlib import Path
import tempfile

codes = set(aliases.values())

def joinpath(root, *other):
    return Path.joinpath(root, *other)

def joinpath_to_cwd(*other):
    return joinpath(Path.cwd(), *other)

def joinpath_to_home(*other):
    return joinpath(Path.home(), *other)

def local_uri_to_path(uri):
    return Path(uri[7:]) # len('file://') == 7

def mktemp(suffix = '', prefix=tempfile.template, dir=None):
    return Path(tempfile.mktemp(suffix, prefix, dir))
