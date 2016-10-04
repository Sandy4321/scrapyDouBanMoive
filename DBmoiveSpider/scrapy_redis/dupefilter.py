from scrapy.dupefilter import BaseDupeFilter
import redis
import time
from scrapy.utils.request import request_fingerprint

class RFPDupeFilter(BaseDupeFilter):
    def __init__(self, server, key):
        self.server = server
        self.key = key

    @classmethod
    def from_settings(cls, settings):
        host = settings.get('REDIS_HOST', 'localhost')
        port = settings.get('REDIS_PORT', 6379)
        server = redis.StrictRedis(host, port)
        key = "dupefilter:%s" % int(time.time())
        return cls(server, key)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):
        '''
        利用redis中的set集合，因为是hash实现，插入删除查找O（1）
        '''
        fp = request_fingerprint(request)
        # 判断去重：如果当前资源的fp在此key下的set中，直接退出，因为重复
        if self.server.sismember(self.key, fp):
            return True
        self.server.sadd(self.key, fp)
        return False

    def close(self, reason):
        self.server.delete(self.key)
