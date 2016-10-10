import random
from base64 import encodebytes

class CustomerProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % proxy['ip_port']
        print("-----------Proxy-----------" + proxy['ip_port'])


PROXIES = [
    {'ip_port': '124.88.67.17:843'},
    {'ip_port': '202.171.253.72:80'},
    {'ip_port': '78.89.180.167:80'},
    {'ip_port': '211.143.45.216:3128'},
    {'ip_port': '113.31.27.228:8080'},
    {'ip_port': '119.6.136.122:843'},
    {'ip_port': '61.162.223.41:9797'},
    {'ip_port': '123.125.122.224:80'},
    {'ip_port': '124.88.67.23:843'},
    {'ip_port': '119.29.253.167:8888'},
    {'ip_port': '111.23.4.139:80'},
    {'ip_port': '124.88.67.23:81'},
    {'ip_port': '123.125.122.224:80'},
]