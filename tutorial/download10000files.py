import mechanize
import cookielib
import time
import os
import json
from sets import Set
import lxml.html
import codecs
import re
from bs4 import BeautifulSoup
import textwrap
# with codecs.open(file name,'r',encoding='utf8') as f:
#     text = f.read()
# # process Unicode text


def strStr(haystack, needle):
        if len(haystack) < len(needle): return -1
        i = 0
        while i < len(haystack)-len(needle)+1:
            j = 0; k = i
            while j < len(needle):
                if haystack[k] == needle[j]:
                    j+=1; k+=1
                else:
                    break
            if j == len(needle):
                break
            else:
                i+=1
        if i == len(haystack)-len(needle)+1:
            return -1
        else:
            return i


def remove(visible_texts, needle):
    buffer = ''
    index = -1
    index = strStr(visible_texts, needle)
    if index != -1:
        buffer += visible_texts[:index]
        buffer += visible_texts[index + len(needle):]
    else:
        buffer = visible_texts
    return buffer


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title', 'link', 'a']:
        return False
    return True


def filteralpha(str):
    str = re.sub(r'([^\s\w]|_)+', '', str)
    return " ".join(str.split(' '))



path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/uniquename.txt")
urlfile=open(path, 'r')
listOfUrl = urlfile.read().split('\n')
print(len(listOfUrl))


i = 2598
from sys import path
c = os.getcwd()
os.chdir('/Users/Xiaomin/cs410hw2')


for url in listOfUrl:
    cj = cookielib.LWPCookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.set_debug_http(True)
    br.set_debug_redirects(True)
    br.set_debug_responses(True)
    br.open(url)
    st = br.response().read()
    #filename = url['name'].split('?q=')[1].split('&btn')[0]
    t = lxml.html.parse(url)
    title = t.find(".//title").text
    file = open('xxu46_'+ str(i) + '.html', 'wb')
    file.write(st)
    file.close()
    #nonjs = re.subn(r'<(script).*?   </\1>(?s)', '', str(st))[0]
    soup = BeautifulSoup(st)
    texts = soup.findAll(text=True)
    visible_texts = filter(visible, texts)
    visible_texts = ''.join(visible_texts)
    needle = '[if IE]><link rel="stylesheet" type="text/css" href="http://ia.media-imdb.com/images/G/01/imdb/css/site/consumer-navbar-ie-470687728._CB379390980_.css"><![endif]'
    visible_texts = remove(visible_texts, needle)
    needle = '<br>'
    visible_texts = remove(visible_texts, needle)
    needle = '<a href="/register/sharing">enable Facebook sharing</a>'
    visible_texts = remove(visible_texts, needle)
    visible_texts = filteralpha(visible_texts)

    with codecs.open('xxu46_' + str(i) + '.txt', 'w', encoding='utf8') as txt:
        txt.write(url+'\n')
        txt.write(title+'\n')
        txt.write(''.join(visible_texts))
        txt.close()
    i += 1
    time.sleep(1)






#
#     import urllib
# >>> html = urllib.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
#
# >>>
# >>> soup = BeautifulSoup(html)
# >>> texts = soup.findAll(text=True)
# >>>
# >>> def visible(element):
# ...     if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
# ...         return False
# ...     elif re.match('<!--.*-->', str(element)):
# ...         return False
# ...     return True
# ...
# >>> visible_texts = filter(visible, texts)
# >>> print visible_texts



