#!/usr/bin/env python
# encoding: utf-8
"""
A Name generator of the form "Adjetive Noum"
===========================================

Install it by:

::

    pip install namegenerator

Use it from the command line

::

    $ python -m namegenerator

Or in your code

::

    from namagenerator import get_random_name
"""

from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='namegenerator',
    version='1.0',
    author='Mario César Señoranis Ayala',
    author_email='mariocesar.c50@gmail.com',
    url='https://github.com/mariocesar/namegenerator',
    long_description=__doc__,
    packages=find_packages()
)