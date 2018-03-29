#coding:utf-8
import requests
# 按照流的方式
r=requests.get('http://www.baidu.com',stream=True)
r.encoding='utf-8'
print 'response--->%s' % r.raw.read()
print 'response--->%s' % r.raw.read(100)
