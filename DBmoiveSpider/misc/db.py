import pymongo
import redis

client = pymongo.MongoClient('localhost', 27017)

db = client['dbmoive']

redis = redis.StrictRedis(host='localhost',port=6379,db=0) #默认设置