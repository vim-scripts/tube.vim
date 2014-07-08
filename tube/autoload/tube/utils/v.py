# -*- coding: utf-8 -*-
"""
tube.utils.v
~~~~~~~~~~~~

This module defines thin wrappers around vim commands and functions.
"""

import vim


def eval(expr, fmt=None):
    """To evaluate an expression."""
    val = vim.eval(expr)
    if fmt is bool:
        return False if val == '0' else True
    elif fmt is int:
        return int(val)
    else:
        return val


def exe(cmd):
    """To execute a vim command."""
    vim.command(cmd)


def echo(msg, hlgroup=""):
    """To display a message to the user via the command line."""
    if hlgroup:
        exe(u"echohl {0}".format(hlgroup))
    exe(u'echo "{0}"'.format(msg).replace('"', '\"'))
    exe("echohl None")
