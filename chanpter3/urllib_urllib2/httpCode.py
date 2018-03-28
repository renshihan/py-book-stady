# coding:utf-8
# 获取HTTP 响应吗
# 对于其他返回码，urlopen会抛出异常，这时候，检查对象code的属性
import urllib2
try:
    print urllib2.urlopen('http://www.baidu.com').getcode()
except urllib2.HTTPError as e:
    if hasattr(e,'code'):
        print 'Error code:',e.cide
