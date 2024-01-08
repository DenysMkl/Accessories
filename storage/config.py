import os


MONGO_URI = os.getenv('MONGODB_URL', 'mongodb://localhost:27017/')
DATABASE_NAME = os.getenv('dbname', 'Accessories')
