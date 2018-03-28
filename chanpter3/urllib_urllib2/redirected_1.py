#coding:utf-8
# 重定向 默认情况下会对Http 3xx返回码自动进行重定向，要检查是否发生重定向动作，只要检查一下Referer的URL和Request的URL是否一致就行了，


import urllib2

response = urllib2.urlopen('http://www.zhihu.com')
print response.geturl()=="http://www.zhihu.com"

print '地址为:response.geturl()---%s' % response.geturl()

