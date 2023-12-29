import json
import os

MONGO_URI = os.getenv('database', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('dbname', 'Accessories')

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
