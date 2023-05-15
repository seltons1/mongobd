from typing import Dict, List
from bson.objectid import ObjectId

class UserRepository():

    def __init__(self, db_connection) -> None:
        self.__collection_name = "user"
        self.__db_connection = db_connection
    
    def insert_document(self, document:Dict) -> Dict:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filter) -> List[Dict]:

        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, # filter
                               {"_id":0}) # filter options)
        
        response = []
        for elem in data: response.append(elem)
        
        return response
    
    def select_one(self, filter) -> Dict:

        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter,{"_id":0})
        return response

    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"age":{"$exists":True}})
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_many_order(self, filter):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, # filter
                               {"_id":0}).sort([("pedidos.monitor",-1)]) # filter options)
        
        response = []
        for elem in data: response.append(elem)
        
        return response
    
    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"$or":[{"name":"samyang"},{"age":{"$exists":True}}]})
        response = []
        for elem in data: response.append(elem)
        return response

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"_id": ObjectId("645ce1e911db6f2d168571a7")})
        response = []
        for elem in data: response.append(elem)
        return response