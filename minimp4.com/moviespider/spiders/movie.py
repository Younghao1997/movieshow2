# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from .. import items

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['minimp4.com']
    url = 'http://minimp4.com/movie/?page='
    offset = 1
    start_urls = [url+str(offset)]

    rules = (
        Rule(LinkExtractor(allow=r'http://minimp4.com/item/\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = items.MoviespiderItem()
        item['mid'] = response.xpath("//tr/td[2]/div/a[1]/@mid").extract()[0]
        item['mname'] = response.xpath("//div[@class='movie-meta']//h1/text()").extract()[0]
        item['mtype'] = response.xpath("//div[@class='movie-meta']/p[4]/a[1]/text()").extract()[0]
        item['mdate'] = response.xpath("//div[@class='movie-meta']/p[7]/text()").extract()[0]
        item['mpoint'] = response.xpath("//div[@class='movie-meta']//p/a[@class='score']/text()").extract()[0]
        item['marea'] = response.xpath("//div[@class='movie-meta']/p[5]/a[1]/text()").extract()[0]
        item['mtime'] = response.xpath("//div[@class='movie-meta']/p[8]/text()").extract()[0]
        item['mresource'] = response.xpath("//tr/td[@class='text-break']/div/a[1]/@href").extract()  # list
        item['mimageurl'] = response.xpath("//div//a[@class='movie-post']//img/@src").extract()[0]  # list
        pwd = response.xpath("//tr/td[2]/div//strong/text()").extract()  # 百度云盘密码
        if not pwd:
            item['mbdpwd'] = ""
        else:
            item['mbdpwd'] = pwd[0]
        yield item
        if self.offset <= 1:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset))
