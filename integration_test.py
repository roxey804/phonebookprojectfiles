

#--------------Integration testing of the phonebook functions--------#

from functions import *


class TestEngine():
    def __init__(self):
        self.pb = Phonebook()

    def test_check_db(self):
        self.checked = self.pb.check_db()
        return self.checked

    def test_connect_db(self):
        self.test_check_db()

        if self.checked:
            connected = self.pb.connect_db()  #IF connected to db: 
            if connected:
                self.connected = True
                print("Connedted to databse")   #all ok
                return self.connected
            else:
                self.connected = False          #IF EXISTS but NOT connected - check connection
                print("Nor Connected check Database connection")
                return self.connected
        else:
            print("Database Does not Exist: Connection Test Failed :-(")

    def test_query_db(self):
        query ="SELECT * FROM business;"
        results = self.pb.query_db(query)
        if results:
            self.queried = True
        else:
            self.query = False
        #if the function returns results, all ok, if not then failed


def test_display_residential(self):
        query ="SELECT * FROM Residential;"
        results = self.pb.display_residential(query)
        if results:
            self.queried = True
        else:
            self.query = False
            
        #if the function returns results, all ok, if not then failed

def test_sort_business_type(self):
    query ="SELECT * FROM Business ORDER BY business_category;"
        results = self.pb.sort_business_type(query)
        if results:
            self.queried = True
        else:
            self.query = False



    def run_tests(self):
        print(self.test_check_db())
        print(self.test_connect_db())
        print(self.test_query_db())
        print(self.test_display_residential())
        print(self.sort_business_type())

    #run tests to check the db, connect to it and query it

if __name__ == "__main__":
    newTest = TestEngine()
    newTest.run_tests()