# -*- coding: utf-8 -*-
from pymongo.cursor import Cursor

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

    @staticmethod
    def filter_diagonal(get_diag, col):
        filter_cases = col.find({'ДІагональ': get_diag},
                                {'_id': 1, 'model': 1,
                                 'price': 1, 'image_link': 1})
        return filter_cases

    @staticmethod
    def filter_volume(get_volume, col):
        hdd_disks_data = []
        if get_volume <= 256 and get_volume != 0:
            hdd_disks_data = col.find({}, {'_id': 1, 'model': 1,
                                           'price': 1, 'image_link': 1})

        return hdd_disks_data

    def close_connection(self):
        self.client.close()
