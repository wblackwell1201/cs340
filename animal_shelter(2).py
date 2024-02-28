from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30715
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True # returns a value of true if in testing
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchTerm):
        if searchTerm is not None: #checking if searchTerm is not empty
            result = self.database.animals.find(searchTerm) #result is set to the list of animals matching the search term
            for animal in result: # iterate through the list of animals
                print(animal) # Prints the animal in the result list
                print("") # new line 
        else: 
            # display error
            raise Exception("Error: nothing to return, search is empty")
        return result # return the list of results
    
    def update(self, searchData, updateData):
        if searchData is not None: # if the data has infomation
            result = self.database.animals.update_many(searchData, { "$set": updateData }) # updates the key value pair to the new data
        else: # if there is not any information to store
            return "{}" # returns nothing
        return result.raw_result # return the result
    
    def delete(self, deleteData):
        if deleteData is not None: # if the data has infomation
            result = self.database.animals.delete_many(deleteData) # deletes the requested data
        else: # if there is not any information to delete
            return "{}" # returns nothing
        return result.raw_result # return result
    
    def cb_render(userValue, passValue, n_clicks, buttonValue):
        
        username = urllib.parse.quote_plus(userValue)
        password = urllib.parse.quote_plus(passValue)
        # instantiating the CRUD object with username and password
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password))
        # set the database to be used as AAC
        self.database = self.client['AAC']
        
        
 