from models.connection_options.connect import DbConnectHandler
from models.repository.user_repository import UserRepository

db_handle = DbConnectHandler()
db_handle.connect_to_db()
connection = db_handle.get_db_connection()

user_repository = UserRepository(connection)
user_repository.insert_document({"name":"AOC","pedidos":{"monitor": 2,"cpu": 10,"estabilizador":5}})

list_of_documents= [
    {"teste":"1"},
    {"teste 2":"2"},
    {"teste 3":"3"},
]
user_repository.insert_list_of_documents(list_of_documents)
response = user_repository.select_many({"name": "Ryzen 2"}) # filter options
print(response)
print(" ")
response2 = user_repository.select_one({"name": "Ryzen 2"})
print(response2)
print(" ")
response3 = user_repository.select_if_property_exists()
print(response3)
print(" ")
response4 = user_repository.select_many_order({"name": "AOC"}) # filter options
print(response4)

print(" ")
response5 = user_repository.select_or() # filter options
print(response5)

print(" ")
response6 = user_repository.select_by_object_id() # filter options
print(response6)



def find(collection: str, key: str, value: str):

    collection_obj = connection.get_collection(collection)

    search_filter = {f'{key}' : f'{value}'}
    #search_filter = {"name" : "Dellaoc"}
    response = collection_obj.find(search_filter)
    for reg in response: print(reg)

def insert(collection: str, values: dict):

    collection_obj = connection.get_collection(collection)

    collection_obj.insert_one(values)
'''
find("user","name","Dellaoc")
insert("user",{"name":"Ryzen 2","size":[55,27,9]})
'''