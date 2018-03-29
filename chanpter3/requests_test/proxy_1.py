#coding:utf-8

import requests

proxie={
    'http':'http://127.0.0.1:8080'
    ,'https':'http://127.0.0.1:8080'
}
r=requests.get('http://example.org',proxies=proxie)
print r.content
