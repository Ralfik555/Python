#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:48:08 2019

@author: rafal
"""

def func():
    print('func() in one.py')
    
def function():
    pass
    
print('Top level in one.py')

if __name__ == '__main__':
    #Make a order with functions if it run directly/ code organization
    function()
    func()