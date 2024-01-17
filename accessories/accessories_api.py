from typing import List

from fastapi import FastAPI

import include_path
import entities
from mongoDB import MongoDB

app = FastAPI()
connect = MongoDB()
counter = 1


@app.get('/{item_type}', response_model=List)
async def get_accessories(item_type: str,
                          volume: int = 0,
                          diagonal: float = 0,
                          model: str = '',
                          page_numb: int = 1,
                          page_size: int = 3):

    global counter
    counter += 1
    get_params = {'volume': volume,
                  'diagonal': diagonal,
                  'model': model}

    accessory = entities.client_code(item_type, **get_params)
    accessory_data = accessory.get_data(connect) if accessory else []

    total_pages = int(len(accessory_data) / page_size)
    try:
        start = (page_numb - 1 + counter % total_pages) * page_size
    except ZeroDivisionError:
        start = 0
    end = start + page_size

    return accessory.get_data(connect)[start:end] if accessory else []
