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
        self.client = pymongo.MongoClient('mongodb://mongo_db/')
        self.db_name = self.client['Accessories']

    @staticmethod
    def delete_data(col) -> None:
        col.delete_many({})

    def connect_to_collection(self, col_name: str):
        my_col = self.db_name[col_name]
        return my_col

    @staticmethod
    def filter_diagonal(get_diag, col):
        if round(get_diag) != get_diag:
            entered_diagonal = get_diag
        else:
            entered_diagonal = int(get_diag)
        diagonal_to_str = f'{entered_diagonal}"'.replace('.', ',')
        filter_cases = col.find({'ДІагональ': diagonal_to_str},
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

    @staticmethod
    def filter_by_prod(get_name, col):
        headphones_data = col.find({}, {'_id': 1, 'model': 1,
                                        'price': 1, 'image_link': 1})
        return headphones_data


    def close_connection(self):
        self.client.close()


# obj = MongoDB()
# coll = obj.db_name['Disks']
# data = coll.find({"model": {'$regex': '1Tb'}})
#
# for i in data:
#     print(i)
