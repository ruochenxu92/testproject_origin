# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from task.models import cs499Item

class SuperqqPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item

import json
class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'wb')
        self.file.write('[')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ", \n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.write(']')
        self.file.close()
