# coding:utf-8
import urllib2
import urllib
url='http://localhost:8080/test/pythonT'
user_agent='Mozilla/4.0(compatible;MSIE 5.5,Windows NT)'
referer="http://www.renshihan.com"
postdata={'username':'renshihan','password':'123456'}
# 将user_agent,referer写入头信息中
headers={'User-Agent':user_agent,'Referer':referer}
data=urllib.urlencode(postdata)
req=urllib2.Request(url,data,headers)
response=urllib2.urlopen(req)
html=response.read()
print  'html:%s' % html