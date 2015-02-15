import mechanize
import cookielib
import time
import os
import json

path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/items.json")
json_data=open(path).read()
data = json.loads(json_data)



i = 0
for url in data:
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
    br.open(url['name'])
    st = br.response().read()
    print len(st)

    #filename = url['name'].split('?q=')[1].split('&btn')[0]

    file = open(str(i) + '.html', 'wb')
    file.write(st)
    file.close()
    check = open(str(i) + '.html', 'r')
    f = check.read()
    print len(f)
    time.sleep( 120 )
    i += 1