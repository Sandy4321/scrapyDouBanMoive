import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['dbmoive']

inserted_collection = db.get_collection('Moives')
