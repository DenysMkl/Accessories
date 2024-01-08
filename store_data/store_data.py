import json

import include_path
from mongoDB import MongoDB


database = MongoDB()


def restore_data(db) -> None:
    for col_name in db.db_name.list_collection_names():
        with open(f'../../data/mongo/{col_name}.json', 'a', encoding='utf-8') as file:
            for obj in db.db_name[col_name].find({}, {}):
                json.dump(obj, fp=file, ensure_ascii=False)
                file.write('\n')


if __name__ == '__main__':
    restore_data(database)
