# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = scrapy.Field()  # 电影ID
    mname = scrapy.Field()  # 电影名称
    mtype = scrapy.Field()  # 电影类型
    mdate = scrapy.Field()  # 上映时间
    mpoint = scrapy.Field()  # 豆瓣评分
    marea = scrapy.Field()  # 制片地区
    mtime = scrapy.Field()  # 电影时长
    mresource = scrapy.Field()  # 电影磁链接
    mbdpwd = scrapy.Field()  # 百度云盘密码
    mimageurl = scrapy.Field()  # 电影封面