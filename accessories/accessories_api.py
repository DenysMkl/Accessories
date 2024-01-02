from typing import List

from fastapi import FastAPI

import include_path
import entities
from mongoDB import MongoDB

app = FastAPI()
connect = MongoDB()


@app.get('/')
async def hello():
    return {'hello': 'world!'}


@app.get('/{item_type}', response_model=List)
async def get_accessories(item_type: str,
                          volume: int = 0,
                          diagonal: float = 0,
                          model: str = '',
                          page_numb: int = 1,
                          page_size: int = 10):

    get_params = {'volume': volume,
                  'diagonal': diagonal,
                  'model': model}
    start = (page_numb - 1) * page_size
    end = start + page_size
    data = entities.client_code(item_type, **get_params)

    return data.get_data(connect)[start:end]
