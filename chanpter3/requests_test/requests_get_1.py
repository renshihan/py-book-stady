#coding:utf-8
# requests是第三方模块，需要额外完成安装
import requests
url='http://www.baidu.com'
r=requests.get(url)

# 响应与编码
print 'content--->%s' % r.content
print 'text---->%s' % r.text
print 'encoding--->%s' % r.encoding

r.encoding='utf-8'
print 'text---->%s' % r.text