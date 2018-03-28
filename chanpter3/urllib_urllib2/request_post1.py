# coding:utf-8
import urllib2
import urllib
url='http://localhost:8080/test/pythonT'
# url='http://www.baidu.com'
postdata={'username':'qiye',
          'password':'qiye_pass'}
# info需要被编码为urllib2能够理解的格式，这里用到的是urllib
data=urllib.urlencode(postdata)
req=urllib2.Request(url,data)
response=urllib2.urlopen(req)
html=response.read()
print html