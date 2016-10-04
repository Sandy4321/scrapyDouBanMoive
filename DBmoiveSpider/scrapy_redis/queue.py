from scrapy.utils.reqser import request_from_dict, request_to_dict
try:
    import cPickle as pickle
except ImportError:
    import pickle

class Base(object):
    """
    Per-spider queue/stack base class
    """
    def __init__(self, server, spider, key):
        self.server = server
        self.spider = spider
        self.key = key % {'spider', spider.name}

    def _encode_request(self, request):
        return pickle.dumps(request_to_dict(request, self.spider), protocol=-1) #protocol=-1即选择最高级的protocol

    def _decode_request(self, encoded_request):
        return request_from_dict(pickle.loads(encoded_request), self.spider)

    def __len__(self):
        raise NotImplementedError

    def push(self, request):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def clear(self):
        self.server.delete(self.key)


class SpiderQueue(Base):
    """
    Per-spider FIFO queue，从头部插入（最先进入的request则在尾部），尾部弹出，实现先进先出
    所以用lpush,rpop
    """
    def __len__(self):
        return self.server.llen(self.key)

    def push(self, request):
        self.server.lpush(self.key, self._encode_request(request))

    def pop(self):
        data = self.server.rpop(self.key)
        if data:
            return self._decode_request(data)

class SpiderPriorityQueue(Base):
    """
    Per-spider priority queue abstraction using redis' sorted set
    """
    def __len__(self):
        return self.server.zcard(self.key)

    def push(self, request):
        data = self._encode_request(request)
        pairs = {data: -request.priority}
        self.server.zadd(self.key, **pairs)

    def pop(self):
        pipe = self.server.pipeline()
        pipe.multi()
        pipe.zrange(self.key, 0, 0).zremrangebyrank(self.key, 0, 0)
        results, count = pipe.execute()
        if results:
            return self._decode_request(results[0])

class SpiderStack(Base):
    """
    Per-spider stack, 先进后出，从头部插入（先进入的request排到尾部），头部弹出（后进入的先弹出），实现后进先出
    """
    def __len__(self):
        return self.server.llen(self.key)

    def push(self, request):
        self.server.lpush(self.key, self._encode_request(request))

    def pop(self):
        data = self.server.lpop(self.key)
        if data:
            return self._decode_request(data)

__all__ = ['SpiderQueue', 'SpiderPriorityQueue', 'SpiderStack']

