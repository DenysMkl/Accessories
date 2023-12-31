import os

from dotenv import load_dotenv


load_dotenv()
MONGO_USER = os.getenv('MONGO_USER', '')
MONGO_PASS = os.getenv('MONGO_PASS', '')
MONGO_URI = os.getenv('database', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('dbname', 'Accessories')
