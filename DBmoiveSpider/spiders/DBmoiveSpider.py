# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from bs4 import BeautifulSoup
import re
from ..items import DbmoivespiderItem




class DBMoiveSpider(CrawlSpider):
    name = "DBmoive"
    allowed_domain = ["movie.douban"]
    start_urls = ["https://movie.douban.com/"]
    rules = {
        Rule(LinkExtractor(allow=r"/subject/\d+/($|\?\w+)"), process_request='process_request',\
             callback='parse_moive', follow=True)
    }
    headers = {
        "accept": "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "text/html; charset=utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76",
        "Referer": "https://movie.douban.com/"
    }
    form_data = {
        'email': 'ziyangsong@foxmail.com',
         'password': 'DIYUJUEWANGszy1'
    }

    def start_requests(self):
        return [Request("https://www.douban.com/accounts/login?source=movie",\
                        meta={'cookiejar': 1}, callback=self.post_login)]


    def post_login(self, response):
        return [FormRequest.from_response(response,
                                          #https://www.douban.com/accounts/login?source=movie"
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,
                                          formdata=self.form_data,
                                          callback=self.after_login,
                                          dont_filter=True)]


    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url, meta={'cookiejar':1}, headers = self.headers, dont_filter=True)


    def process_request(self, request):
        request = request.replace(headers=self.headers)
        return request


    def parse_moive(self, response):
        data = response.body
        soup = BeautifulSoup(data, "html.parser")

        item = DbmoivespiderItem()
        self.get_name(soup, item)
        self.get_director(soup, item)
        self.get_country(response, item)
        self.get_time(soup, item)
        self.get_genre(soup, item)
        self.get_voters(soup, item)
        self.get_star(soup, item)
        self.get_every_level_star(soup, item)
        return item


    def get_name(self, soup, item):
        name = soup.find("span", {"property": "v:itemreviewed"})
        item['Name'] = name.get_text()


    def get_director(self, soup, item):
        director = soup.find_all("a", {"rel": "v:directedBy"})
        directors = ""
        for d in director:
            directors = directors + d.get_text()
        item['Director'] = directors


    def get_country(self, response, item):
        '''
        html上的形式为：<span class="pl">制片国家/地区:</span> 日本<br/>
        利用beautifulsoup解析失败....只能用response
        '''
        country_pattern = re.compile(r"制片国家/地区:</span> (.+?)<br>")
        search_info = "".join(response.xpath("//div[@id='info']").extract())
        country = country_pattern.search(search_info)
        item["Country"] = [country.strip() for country in country.group(1).split("/")]
        #group(1)获得country_pattern中的()中的匹配对象


    def get_time(self, soup, item):
        time = soup.find("span", {"class": "year"})
        item['Time'] = time.get_text()


    def get_genre(self, soup, item):
        genres = soup.find_all("span", {"property": "v:genre"})
        genre = ""
        for g in genres:
            genre = genre + g.get_text()
        item['Genre'] = genre


    def get_voters(self, soup, item):
        voters = soup.find("span", {"property": "v:votes"})
        item['Voters'] = voters.get_text()


    def get_star(self, soup, item):
        star = soup.find("strong", class_="ll rating_num", property="v:average")
        item['Star'] = soup.find = star.get_text()


    def get_every_level_star(self, soup, item):
        every_level_star = soup.find_all("span", {"class": "rating_per"})
        star_distribution = ""
        for one_level_star in every_level_star:
            star_distribution = star_distribution + one_level_star.get_text()
        item['StarDistribution'] = star_distribution

