#!/usr/bin/env python
# encoding: utf-8
"""
A Name generator of the form "Adjetive Noun"
============================================

Install it by. ::

    pip install codenamegenerator

Use it from the command line ::

    $ python -m codenamegenerator

Or in your code ::

    from codenamagenerator import get_random_name

"""

from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='codenamegenerator',
    version='1.3',
    author='Mario César Señoranis Ayala',
    author_email='mariocesar.c50@gmail.com',
    url='https://github.com/mariocesar/codenamegenerator',
    description='A Name generator of the form "Adjetive Noun"',
    long_description=__doc__,
    packages=find_packages(),
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
)
