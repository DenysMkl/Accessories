import json

import include_path
from mongoDB import MongoDB


database = MongoDB()


def restore_data(db) -> None:
    for col_name in db.db_name.list_collection_names():
        with open(f'../../data/mongo/{col_name}.json', 'w') as file:
            json.dump(list(db.db_name[col_name].find({}, {})), fp=file, indent=4)


if __name__ == '__main__':
    restore_data(database)
