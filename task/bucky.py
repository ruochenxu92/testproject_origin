__author__ = 'Xiaomin'

import requests
from bs4 import BeautifulSoup

class bucky:
    def trade_spider(self):
        #page = 1
        #while page < max_pages:
        url = 'https://courses.engr.illinois.edu/cs225/'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        list = []
        for link in soup.findAll('a'):
            href = url + str(link.get('href'))
            list.append(href)
        return list

    def get_single_item_data(self):
        f = open('testfile', 'w')
        list = []
        list = self.trade_spider()
        count = 0
        for item_url in list:
            source_code = requests.get(item_url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            for item_name in soup.findAll('p'):
                #f.write(item_name.text)
                count += len(item_name.text)
        f.close()
        print("total num",count)

b = bucky()
b.get_single_item_data()







