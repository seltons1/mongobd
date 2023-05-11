from connect import DbConnect

connection = DbConnect().mongo_connection()
print(connection)
def find(collection: str, key: str, value: str):

    collection_obj = connection.get_collection(collection)

    #search_filter = {f'{key}' : f'{value}'}
    search_filter = {"name" : "Dellaoc"}
    response = collection_obj.find(search_filter)
    for reg in response: print(reg)


find("user","name","Dellaoc")
