# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:09:41 2019

@author: RN
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:09:16 2019

@author: RN
"""



#---------------------------------
## CHAPTER 14 -- Phonebook project
#---------------------------------

import sqlite3
import json
import time


#-------------------------------------------------------
# Connect to the database
#-------------------------------------------------------
conn = sqlite3.connect("phonebook_project.db")
c = conn.cursor()
#-------------------------------------------------------
# Functions
#-------------------------------------------------------

#-------------------------------------------------------
# Extracting and using data from database
#-------------------------------------------------------
 
#---------------------------------
## Residential Search
#---------------------------------

##---- 1) Ask User input for 'surname' 

def ask_surname():
    surname = input("What's the surname of the person you are looking for?")
    c.execute('SELECT * FROM Residential WHERE surname = ?', (surname.title(),))
    surname_results = c.fetchall()
    if len(surname_results) <1:  #    if this is empty using length of list then you print error
        print("Sorry, name not in phonebook")
    else:
        print ("We found",len(surname_results),"results")
        time.sleep(2)
        print(surname_results)
        
  

#---- 2) The user searches by the  their location :
        
def Residential_ask_location():
    town_city = input("What city or town do you want to search within?")
    c.execute('SELECT * FROM Residential WHERE town_city = ?', (town_city.title(),))
    location_results = c.fetchall()
    if len(location_results) <1:  #    if this is empty using length of list then you print error
        print("Sorry, there are no results for that location")
    else:
        print ("We found",len(location_results),"results")
        time.sleep(2)
        print(location_results)
        sorting_choice = input("Do you want to sort results by surname, alphabetically? y/n: ")
        if sorting_choice[0] == "y":
            return sort_surname(location_results)
        else:
            print(location_results)

#---- 3) The user is presented with the relevant GROUP BY 'surname' AND 'location' 

def sort_surname(location_results):
    sorted_by_surname = sorted(location_results, key=lambda tuple:tuple[1])
    print(sorted_by_surname)
   
#ask_surname()

#---- 4) Ask the user if they want to sort the returned results by distance from
#    location:
#       if yes:
#           then order the returned group by results by the distance to location.
#       else:
#           return the a-z sorted results
#-------------------------------------------------------
# MVP - Residential subfunctions
#-------------------------------------------------------
def display_residential():
    conn = sqlite3.connect("phonebook_project.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Residential')
    surname_results = c.fetchall()
    return surname_results
    #print(surname_results)        


def sort_residential_location():
    db = connectdb()
    loc_data = input("What city or town do you want to search within? ").title()
    db.execute('SELECT * FROM Residential WHERE town_city = ?', (loc_data,))
    for row in db.fetchall():
        print (row)
        
#---------------------------------
## MVP--Business Pseudo Code
#---------------------------------

#---- 1) Ask User input for 'type' or 'name':
def user_input_business():
    businesschoice = input("Would you like to search for business type or business name? ")
    if businesschoice == "type":
        print ("You chose business type")
        time.sleep(1)
        sort_business_type()
    elif businesschoice == "name":
        print ("You chose business name")
        time.sleep(1)
        sort_business_name()
    else:
        print ("Error, please try again")
        return user_input_business()
#
#---- 1.1) Ask User input if they want to sort by loaction rather than a-z 
#        if input is a valid string
#           render data sorted by location. 
#        else tell the user they need a valid input.

#-------------------------------------------------------
# MVP - Business subfunctions
#-------------------------------------------------------
        
#--------# Sorting business data #----------
        
def sort_business_type():
    conn = sqlite3.connect("phonebook_project.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Business ORDER BY business_category')
    business_type_results = c.fetchall()
    return business_type_results
        
def sort_business_name():
    conn = sqlite3.connect("phonebook_project.db")
    c = conn.cursor()
    c.execute('SELECT * FROM Business ORDER BY business_name')
    business_name_results = c.fetchall()
    return business_name_results
#    for row in c.fetchall():
#        print (row[0])

def sort_business_location():
    db = connectdb()
    loc_data = input("please enter the town or city: ").title()
    time.sleep(1)
    db.execute('SELECT * FROM Business WHERE town_city = ?', (loc_data,))
    for row in db.fetchall():
        print (row)
        
       
