import mechanize
import cookielib
import time
import os

path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/google1.txt")
f = open(path)
listOfP = f.read().split('\n')
i = 0
for url in listOfP:
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
    br.open("https://scholar.google.com/citations?user=FANRIhwAAAAJ&hl=en&oi=ao")
    file = open('scholargoogle.html', 'wb')
    st = br.response().read()
    print st
    file.write(st)
    file.close()
    #filename = url.split('?q=')[1].split('&btn')[0]
    file = open(str(i) + '.html', 'wb')
    time.sleep( 30 )
    i += 1