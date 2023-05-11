from models.connection_options.connect import DbConnectHandler

db_handle = DbConnectHandler()
db_handle.connect_to_db()
connection = db_handle.get_db_connection()

def find(collection: str, key: str, value: str):

    collection_obj = connection.get_collection(collection)

    search_filter = {f'{key}' : f'{value}'}
    #search_filter = {"name" : "Dellaoc"}
    response = collection_obj.find(search_filter)
    for reg in response: print(reg)

def insert(collection: str, values: dict):

    collection_obj = connection.get_collection(collection)

    collection_obj.insert_one(values)

find("user","name","Dellaoc")
insert("user",{"name":"Ryzen 2","size":[55,27,9]})
