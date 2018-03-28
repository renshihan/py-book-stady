#coding:utf-8
# 需要某个cookie项的值
import urllib2
import cookielib
import test_init

opener=urllib2.build_opener()
opener.addheaders.append(('Cookie','email=%s' % '37959548@qq.com'))
req=urllib2.Request('http://www.zhihu.com/')
response=opener.open(req)
print 'response.headers:%s'% response.headers
redata=response.read()
print '接收到的数据:\r\n%s' % redata
