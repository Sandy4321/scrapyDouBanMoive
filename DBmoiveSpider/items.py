# -*- coding: utf-8 -*-
import scrapy


class DbmoivespiderItem(scrapy.Item):
    _id = scrapy.Field()
    Name = scrapy.Field()       #电影名
    Director = scrapy.Field()   #导演
    Country = scrapy.Field()    #制作国家
    Time = scrapy.Field()       #制作时间
    Genre = scrapy.Field()      #分类
    Voters = scrapy.Field()     #投票人数
    Star = scrapy.Field()       #分数
    StarDistribution = scrapy.Field()   #星级分配




