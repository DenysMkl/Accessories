import json

import pymongo

import include_path
from mongoDB import MongoDB


database = MongoDB()

for col_name in database.db_name.list_collection_names():
    with open(f'{col_name}.json', 'w') as file:
        json.dump(list(database.db_name[col_name].find({}, {})), fp=file, indent=4)