#!/usr/bin/env python

from distutils.core import setup

setup( name='clewareADC',
       version='0.1',
       description='Python module to read values from Cleware USB-ADC 2',
       author='Johannes Koch',
       author_email='johannes@ortsraum.de',
       license='MIT',
       packages=['clewareADC'],
       requires=['hidapi'],
     )

