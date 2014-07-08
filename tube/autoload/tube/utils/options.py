# -*- coding: utf-8 -*-
"""
tube.utils.options
~~~~~~~~~~~~~~~~~~

This module defines just the `get` function. This function retrieves
Tube options.
"""

from tube.utils import v


prefix = 'g:tube_'


def get(name, fmt=None):
    """To get the value of a Tube setting."""
    if not v.eval(u"exists('{0}')".format(prefix + name), fmt=bool):
        raise ValueError("Option '{0}' does not exist".format(prefix + name))
    return v.eval(prefix + name, fmt=fmt)
