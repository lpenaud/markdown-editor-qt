#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
from enum import Enum
import helpers

class GTK_ICON_THEME_SCHEMA(Enum):
    GNOME = 'org.gnome.deskop.interface'
    CINNAMON = 'org.cinnamon.deskop.interface'
    MATE = 'org.mate.interface'

def get_xfce_icon_theme():
    cmd = (
        'xfconf-query',
        '-lvc',
        'xsettings',
        '-p',
        '/Net/ThemeName',
    )
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = str(p.stdout.read())
    return out.split(' ')[2][:-3]

def get_gtk_icon_theme(schema):
    cmd = (
        'gsettings',
        'get',
        schema.value,
        'icon-theme',
    )
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = str(p.stdout.read())
    return out.split("'")[1]

def get_desktop_environnement():
    current = os.environ.get('DESKTOP_SESSION', 'GNOME')
    available = [member.name for member in GTK_ICON_THEME_SCHEMA]
    if current in available:
        return current
    if 'xfce' in current:
        return 'xfce'
    return GTK_ICON_THEME_SCHEMA.GNOME

def get_current_system_icon_theme():
    if helpers.on_linux():
        current = os.environ.get('DESKTOP_SESSION', 'GNOME').upper()
        if 'XFCE' in current.capitalize():
            return get_xfce_icon_theme()
        for member in GTK_ICON_THEME_SCHEMA:
            if member.name in current:
                return get_gtk_icon_theme(member)
    return 'tango'
