from typing import List

from fastapi import FastAPI

from accessories.storage.mongoDB import MongoDB
from accessories import entities

app = FastAPI()
connect = MongoDB()


@app.get('/')
async def hello():
    return {'hello': 'world'}

@app.get('/{item_type}', response_model=List)
async def get_accessories(item_type: str,
                          volume: int = 0,
                          diagonal: float = 0,
                          model: str = ''):
    get_params = {'volume': volume,
                  'diagonal': diagonal,
                  'model': model}

    data = entities.client_code(item_type, **get_params)

    return data.get_data(connect)
