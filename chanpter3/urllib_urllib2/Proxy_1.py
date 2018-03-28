#coding:utf-8
import urllib2
# 使用ProxyHandler在程序中动态设置代理
proxy=urllib2.ProxyHandler({'http':'127.0.0.1:8080'})
opener=urllib2.build_opener(proxy)
response=opener.open('http://www.zhihu.com/')
print response.read()