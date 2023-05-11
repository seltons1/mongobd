from connect import DbConnect

connection = DbConnect().mongo_connection()
print(connection)