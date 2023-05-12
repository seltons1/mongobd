from typing import Dict

class UserRepository():

    def __init__(self, db_connection) -> None:
        self.__collection_name = "user"
        self.__db_connection = db_connection
    
    def insert_document(self, document:Dict) -> Dict:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

