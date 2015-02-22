# -*- coding: utf-8 -*-

# Scrapy settings for superqq project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'
SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'superqq (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    #'tutorial.pipelines.JsonWriterPipeline': 2,
    'tutorial.pipelines.SuperqqPipeline': 1,
}

import sys
sys.path.append('/Users/Xiaomin/testproject')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'