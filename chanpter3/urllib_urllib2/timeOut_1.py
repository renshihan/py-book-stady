# coding:utf-8
import urllib2

# url='http://localhost:8080/test/pythonT'
url='http://www.zhifu.com'
request=urllib2.Request(url)
response=urllib2.urlopen(request,timeout=2)
html=response.read()
print '返回数据%s' % html

    