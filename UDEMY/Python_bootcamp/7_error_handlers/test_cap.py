#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:10:45 2019

@author: rafal
"""
import sys
sys.path.append('/home/rafal/Desktop/DataScience/Python_bootcamp/7_error_handlers')


import unittest
import cap


class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')
        
    
    def test_multiple_word(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

       
if __name__ == '__main__':
    unittest.main()


        