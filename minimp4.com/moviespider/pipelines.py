# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from . import settings
import requests


class MoviespiderPipeline(object):
    def __init__(self):
        self.filename = open("movie.json", 'w')

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        dir_path = '%s/%s/%s' % (settings.IMAGES_STORE, spider.name, item['mid'])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['mimageurl']:
            if image_url == '无插图':
                break
            image_file_name = image_url.split('/')[-1]
            file_path = '%s/%s' % (dir_path, image_file_name)
            if os.path.exists(file_path):
                continue

            with open(file_path, 'wb') as handle:
                response = requests.get(image_url, stream=True)
                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
        return item

    def close_spider(self, spider):
        self.filename.close()
