#!/usr/bin/env python
# encoding: utf-8
"""
A Name generator of the form "Adjetive Noun"
============================================

Install it by. ::

    pip install codenamegenerator

Use it from the command line ::

    $ python -m codenamegenerator --help

Or in your code ::

    from codenamegenerator import generate_codenames
    print(generate_codenames())

"""

from setuptools import setup, find_packages


setup(
    name="codenamegenerator",
    version="2.1.0",
    author="Mario César Señoranis Ayala",
    author_email="mariocesar.c50@gmail.com",
    url="https://github.com/mariocesar/codenamegenerator",
    description='A Name generator of the form "Adjetive Noun"',
    long_description=__doc__,
    packages=find_packages(),
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
