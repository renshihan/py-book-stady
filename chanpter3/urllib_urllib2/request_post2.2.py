# coding:utf-8
import urllib2
import urllib
url='http://localhost:8080/test/pythonT'
user_agent='Mozilla/4.0(compatible;MSIE 5.5,Windows NT)'
referer="http://www.renshihan.com"
postdata={'username':'renshihan','password':'123456'}
# 将user_agent,referer写入头信息中
data=urllib.urlencode(postdata)
req=urllib2.Request(url)
req.add_header('User-Agent',user_agent)
req.add_header('Referer',referer)
req.add_data(data)
response=urllib2.urlopen(req)
html=response.read()
print  'html:%s' % html