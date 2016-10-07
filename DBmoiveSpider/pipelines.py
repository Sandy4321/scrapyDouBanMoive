# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .misc.db import inserted_collection

class DBmoiveSpiderPipeline(object):
    def process_item(self, item, spider):
        result = inserted_collection.insert_one(item)
        return item
