from scrapy.downloadermiddlewares.defaultheaders import DefaultHeadersMiddleware


class CustomerHeaderMiddleware(DefaultHeadersMiddleware):
    headers = {
        "accept": "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76",
        "Referer": "https://movie.douban.com/"
    }
    def process_request(self, request, spider):
        request.headers["accept"] = self.headers["accept"]
        request.headers["Accept-Encoding"] = self.headers["Accept-Encoding"]
        request.headers["Accept-Language"] = self.headers["Accept-Language"]
        request.headers["Connection"] = self.headers["Connection"]
        request.headers["Content-Type"] = self.headers["Content-Type"]
        request.headers["User_Agent"] = self.headers["User-Agent"]
        request.headers["Referer"] = self.headers["Referer"]
        return request

