__author__ = 'Obstc0rp'

from distutils.core import setup
import py2exe
import os, sys

setup(console=['PyDFGlue.py'])
os.rename('dist', 'PyDFGlue')