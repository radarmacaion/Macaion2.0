# -*- coding: utf-8 -*-
"""Example NumPy style docstrings.

This module demonstrates documentation as specified by the `NumPy
Documentation HOWTO`_. Docstrings may extend over multiple lines. Sections
are created with a section header followed by an underline of equal length.

Example
-------
Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks::

    $ python example_numpy.py


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented:

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created by
resuming unindented text.




.. _NumPy Documentation HOWTO:
   https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

"""

a = 200.0
"""a ZR"""

b = 1.5
"""b ZR"""


import os
from Modulo1 import Operazione

def Somma(a,b):
   """Funzione somma.
   
   Extended description of function.
   
   Parameters
   __________
   
   a : int
        Il primo addendo
   b : int
        Il secondo addendo
        
   Returns
   _______
   
   int
      Somma due interi
   """
   return a+b



