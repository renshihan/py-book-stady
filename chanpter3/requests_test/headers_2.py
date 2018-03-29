# coding:utf-8
import requests
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}
r=requests.get("http://localhost:8080/test/pythonT",params={'username':'renshihan','password':'123456'},headers=headers)

if r.status_code==requests.codes.ok:
    print '响应码:%s' % r.status_code
    print '响应头:%s' % r.headers
    print '（推荐使用这种方法获取其中某个字段）:%s' % r.headers.get("content-type")
    print '（不推荐这种方法获取）:%s' % r.headers['content-type']
else:
    r.raise_for_status()    #是用来主动往出异常的
# print r.content