from pymongo import MongoClient

class DbConnect():

    @staticmethod
    def mongo_connection():

        connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"
        client = MongoClient(connection_string)

        db_connection = client["dbmongo"]

        return db_connection

