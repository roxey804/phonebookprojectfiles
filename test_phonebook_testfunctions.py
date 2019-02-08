# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:52:58 2019

@author: RN
"""
#--------------------------------------------
## MODULE 03 -- Phonebook -- Validation Tests
#--------------------------------------------
import unittest
from phonebook_testfunctions import *
    
#----- Check for existence of database 

class testDBExists(unittest.TestCase):
    def test_dbexists(self):
        self.assertTrue(True)
    

class testfuncs(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, checksurnameinput, 4) #if type is int
        self.assertRaises(TypeError, checksurnameinput, True) #if boolean
        
    
if __name__ == "__main__":
    unittest.main()