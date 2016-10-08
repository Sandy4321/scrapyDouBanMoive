# -*- coding: utf-8 -*-

BOT_NAME = 'DBmoiveSpider'

SPIDER_MODULES = ['DBmoiveSpider.spiders']
NEWSPIDER_MODULE = 'DBmoiveSpider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


DOWNLOAD_DELAY = 0.2
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 128
#The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain.

COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DBmoiveSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
   'DBmoiveSpider.misc.UserAgentMiddleware.CustomerUserAgentMiddleware': 400
}

USER_AGENT = ''

ITEM_PIPELINES = {
   'DBmoiveSpider.pipelines.DBmoiveSpiderPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3 # The initial download delay
AUTOTHROTTLE_MAX_DELAY = 60  # The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0# The average number of requests Scrapy should be sending in parallel to each remote server


# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


LOG_LEVEL = "INFO"

#深度优先
DEPTH_LIMIT = 0 #爬取网站最大允许的深度(depth)值。如果为0，则没有限制
DEPTH_PRIORITY = 0 #如果为0，则不根据深度进行优先级调整
DNSCACHE_ENABLED = True #启用DNS内存缓存(DNS in-memory cache)

#
# import sys
# sys.setrecursionlimit(1000000)

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379