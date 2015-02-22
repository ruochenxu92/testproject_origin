# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class WikiItem(scrapy.Item):
    name = Field()
    value = Field()

from task.models import cs499Item
from scrapy.contrib.djangoitem import DjangoItem

class PersonItem(DjangoItem):
    django_model = cs499Item

