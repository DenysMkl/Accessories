import os

MONGO_URI = os.getenv('database', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('dbname', 'Accessories')