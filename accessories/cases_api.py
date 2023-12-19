from typing import List

from fastapi import FastAPI

from accessories.storage.mongoDB import MongoDB


app = FastAPI()
connect = MongoDB()


@app.get('/items/{item_type}', response_model=List)
def get_accessories(item_type: str):
    data = connect.get_data(item_type)
    return data