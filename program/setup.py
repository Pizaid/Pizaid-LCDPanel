#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://github.com/Pizaid
# License:  2-Clause BSD License
# Created:  2014-07-12
#

from setuptools import setup, find_packages

setup(name='pizaid-lcdserver',
      version='0.0.1',
      description='Pizaid LCD Panel Controller',
      author='Pizaid Developer Team',
      url='https://github.com/Pizaid',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      pizaid_lcdserver = pizaid:start
      """)
