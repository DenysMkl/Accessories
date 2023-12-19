# -*- coding: utf-8 -*-
import config
import pymongo


class SingleDB(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MongoDB(metaclass=SingleDB):
    def __init__(self):
        self.client = pymongo.MongoClient(config.MONGO_URI)
        self.db_name = self.client[config.DATABASE_NAME]

    def connect_to_collection(self, col_name: str):
        my_col = self.db_name[col_name]
        return my_col

    def get_data(self, col_name: str):
        collection = self.connect_to_collection(col_name.title())
        data = collection.find({}, {'_id': 1, 'model': 1, 'price': 1, 'image_link': 1})
        return data

    def close_connection(self):
        self.client.close()