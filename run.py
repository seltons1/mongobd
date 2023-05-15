from models.connection_options.connect import DbConnectHandler
from models.repository.user_repository import UserRepository

db_handle = DbConnectHandler()
db_handle.connect_to_db()
connection = db_handle.get_db_connection()

user_repository = UserRepository(connection)
user_repository.insert_document({"name":"AOC","val":[5,9,6]})

list_of_documents= [
    {"teste":"1"},
    {"teste 2":"2"},
    {"teste 3":"3"},
]
user_repository.insert_list_of_documents(list_of_documents)




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