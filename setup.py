#!/usr/bin/env python
# encoding: utf-8
"""
A Name generator of the form "Adjetive Noun"
============================================

Install it by. ::

    pip install namegenerator

Use it from the command line ::

    $ python -m namegenerator

Or in your code ::

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
    description='A Name generator of the form "Adjetive Noun"',
    long_description=__doc__,
    packages=find_packages(),
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.4'
    ],
)