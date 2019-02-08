#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:20:44 2019

@author: matildaoswell-wheeler
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:49:07 2019

@author: RN
"""


def check_db_exists(f):
    try:
        f = open ("phonebook_project.db")
        f.close()
        print("file found")
#        return True
    except FileNotFoundError:
        print("file not found")

#check_db_exists()
    
def checksurnameinput(surname):
    if type(surname) not in [str]:
        raise TypeError("the input must be a string")
        
     
#--------------------------------------------------------#
        

        
