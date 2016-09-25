# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .misc.db import db

class DbmoivespiderPipeline(object):
    collection_name = 'moives'

    def process_item(self, item, spider):
        required_collection = db.get_collection(self.collection_name)
        result = required_collection.insert_one(item)
        return item
