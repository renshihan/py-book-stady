#coding:utf-8
import requests
# 自定义cookie值发送出去，可以使用以下方法，示例如下：
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}

cookies=dict(name='renshihan',age='123')

# r=requests.get("http://localhost:8080/test/pythonT",params={'username':'renshihan','password':'123456'},headers=headers)
r=requests.get("http://www.baidu.com",headers=headers,cookies=cookies)



print r.text



