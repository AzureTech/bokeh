#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' ``TextLike`` is a shortcut for properties that accepts strings, parsed
strings, and text-like objects, e.g.:

* :class:`~bokeh.models.text.MathText`
* :class:`~bokeh.models.text.PlainText`

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from .either import Either
from .instance import Instance
from .primitive import String

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    "TextLike",
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def converter(value: str):
    print("textlikeconverter value:", value)
    if len(value) >= 2 and value[0] == value[-1] == "$":
        print('here')
        from ...models.text import TeX
        return TeX(text=value[1:-1])
    return value

TextLike = Either(
    String,
    Instance("bokeh.models.text.BaseText"),
).converts(String, converter)

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
