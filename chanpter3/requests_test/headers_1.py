# coding:utf-8
import requests
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}
r=requests.get("http://localhost:8080/test/pythonT",params={'username':'renshihan','password':'123456'},headers=headers)
print r.content