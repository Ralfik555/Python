#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:52:08 2019

@author: rafal
"""
import sys
sys.path.append('/home/rafal/Desktop/DataScience/Python_bootcamp')


from mymodule import myfunc

from myMainPackage import some_main_script
from myMainPackage.SubPackage import my_sub_script

some_main_script.sub_report_main()
my_sub_script.sub_report()