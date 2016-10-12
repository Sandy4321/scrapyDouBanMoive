# -*- coding: utf-8 -*-
import pymongo


class DBmoiveSpiderPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['DoubanMoive']
        self.collection  = db.get_collection('Moives')

    def process_item(self, item, spider):
        result = self.collection.insert_one(item)
        return item
