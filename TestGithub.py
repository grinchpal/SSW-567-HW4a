# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from github import my_function

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNoRepo(self): 
        self.assertEqual(my_function("test20"),"user test20 doesn't have any public repos")
        print(my_function("test20"))

    def testValidUsername(self): 
        self.assertEqual(my_function(";aksjdf;kajsd;fkj"),"user ;aksjdf;kajsd;fkj doesn't exist")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

