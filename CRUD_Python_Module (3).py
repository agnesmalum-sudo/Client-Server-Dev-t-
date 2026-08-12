from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """ Method to insert a document into the database """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, search_criteria):
        """ Method to query documents from the database """
        try:
            cursor = self.collection.find(search_criteria)
            results_list = list(cursor)
            return results_list
        except Exception as e:
            print(f"An error occurred during read: {e}")
            return []

    def update(self, search_criteria, update_data):
        """
        Method to update document(s) in the database.
        search_criteria: dictionary used to find the document(s)
        update_data: dictionary containing the fields to update (must use $set, $inc, etc.)
        Returns: number of documents modified
        """
        if search_criteria is not None and update_data is not None:
            try:
                result = self.collection.update_many(search_criteria, update_data)
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Nothing to update, because data parameter is empty")

    def delete(self, search_criteria):
        """
        Method to delete document(s) from the database.
        search_criteria: dictionary used to find the document(s) to delete
        Returns: number of documents deleted
        """
        if search_criteria is not None:
            try:
                result = self.collection.delete_many(search_criteria)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            raise Exception("Nothing to delete, because data parameter is empty")