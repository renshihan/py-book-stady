#coding:utf-8
# requests是第三方模块，需要额外完成安装
import requests
url='http://localhost:8080/test/pythonT'
dataget={'username':'renshihan','password':'123456'}
#
r=requests.get(url,params=dataget)
print r.content