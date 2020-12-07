#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:49:44 2019

@author: rafal
"""

import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
    print('two.py is being run directly')
else:
    print('two.py has been imported')