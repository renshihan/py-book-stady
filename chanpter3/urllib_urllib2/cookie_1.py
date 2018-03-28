#coding:utf-8
# 需要某个cookie项的值
import urllib2
import cookielib
# url='http://localhost:8080/test/pythonT'
url='http://www.zhihu.com'
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response=opener.open(url)
for item in cookie:
    print 'item.name %s' % item.value
