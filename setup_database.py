

#---------------------------------
## CHAPTER 14 -- Phonebook project
#---------------------------------

import sqlite3
import json
import time
import requests

#-------------------------------------------------------
# Setting up the database 
#-------------------------------------------------------

def connectdb():
    try:     
            conn = sqlite3.connect("phonebook_project.db") #Connects to the database
            cursor = conn.cursor()
            return cursor, conn
    except:
            return False

def create_table():
    db, conn = connectdb() # Connects to db through return cursor output.
    db.execute("CREATE TABLE IF NOT EXISTS Residential(first_name TEXT , surname TEXT, address_line_1 TEXT, town_city TEXT, country TEXT, postcode TEXT, region TEXT, telephone_number REAL)")
    db.execute("CREATE TABLE IF NOT EXISTS Business(business_name TEXT , address_line_1 TEXT, town_city TEXT, country TEXT, postcode TEXT, region TEXT, telephone_number REAL, business_category TEXT)")
    db.execute("CREATE TABLE IF NOT EXISTS Coordinates(postcode TEXT, longitude REAL, latitude REAL)")
   
#create_table()

#-------------------------------------------------------
# Reading in  JSON file 
#-------------------------------------------------------

# JSON residential
residential_file = open('json/residential_data.json')
residential_data = json.load(residential_file)

# JSON business
business_file = open('json/business_data.json')
business_data = json.load(business_file)

#-------------------------------------------------------
# Entering the data into the database 
#-------------------------------------------------------

def data_entry_residential():
    db, conn = connectdb() # Connects to db through return cursor output.
    for row in range(len(residential_data)):
        first_name = residential_data[row]['first_name']
        surname = residential_data[row]['last_name']
        address_line_1 = residential_data[row]['address_line_1']
        town_city = residential_data[row]['address_line_2']
        country = residential_data[row]['address_line_3']
        postcode = residential_data[row]['postcode']
        region = residential_data[row]['country']
        telephone = residential_data[row]['telephone_number']
        db.execute("INSERT INTO Residential (first_name , surname, address_line_1, town_city, country, postcode, region, telephone_number)VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (first_name , surname, address_line_1, town_city, country, postcode, region, telephone))
        conn.commit()  # this commits the data above to our task1 database


#data_entry_residential()
        
#this pulls the data from the json file using the keys defined as new variables (column names)
#the names in 'green' are the json keys, whilst the variables on the RHS are the database column names
        
def data_entry_business():
    db, conn = connectdb() # Connects to db through return cursor output.
    for row in range(len(business_data)):
        business_name = business_data[row]['business name']
        address_line_1 = business_data[row]['address_line_1']
        town_city = business_data[row]['address_line_2']
        country = business_data[row]['address_line_3']
        postcode = business_data[row]['postcode']
        region = business_data[row]['country']
        telephone = business_data[row]['telephone_number']
        business_category = business_data[row]['business_category']
        db.execute("INSERT INTO Business (business_name , address_line_1, town_city, country, postcode, region, telephone_number, business_category)VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (business_name , address_line_1, town_city, country, postcode, region, telephone, business_category))
        conn.commit()  # this commits the data above to our task1 database

#data_entry_business()


def data_entry_coords():
    db, conn = connectdb() # Connects to db through return cursor output.
    for row in range(len(residential_data)):
        postcode = residential_data[row]['postcode']
        no_spaces = postcode.replace(" ", "")
        api_postcode = requests.get("http://api.postcodes.io/postcodes/{}".format(no_spaces))
        postdata = api_postcode.json()
        if postdata['status'] == 200:
            longitude = postdata['result']['longitude']
            latitude = postdata['result']['latitude']
            db.execute('INSERT INTO Coordinates(postcode, longitude, latitude) VALUES(?, ?, ?)', (postcode, longitude, latitude))
        else:
            pass
        conn.commit()
        
#data_entry_coords()

