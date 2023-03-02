from pymongo import MongoClient
import config


class Database():
    def database_connect(self):
        self.client = MongoClient(
            config.DB_KEY)

    def database_dump(self, data):
        db = self.client["database"]
        col = db["user_watchlist"]
        col.insert_one(data)

    def database_load(self):
        db = self.client["database"]
        col = db["user_watchlist"]
        content_data = list(col.find())
        return content_data

    def database_delete_entry(self, unique_id):
        db = self.client["database"]
        col = db["user_watchlist"]
        col.delete_one({"id": unique_id})

    def database_close(self):
        self.client.close()
