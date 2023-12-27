from typing import List

from fastapi import FastAPI
from fastapi.openapi.models import Response

from accessories.storage.mongoDB import MongoDB


app = FastAPI()
connect = MongoDB()


@app.get('/{item_type}', response_model=List)
async def get_accessories(item_type: str,
                          volume: int = 0,
                          diagonal: str = '',
                          model: str = ''):
    get_params = {'volume': volume,
                  'diagonal': diagonal,
                  'model': model}
    data = connect.get_data(item_type, **get_params)
    return data
