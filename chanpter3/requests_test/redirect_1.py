# coding:utf-8
import requests

r=requests.get("http://github.com",allow_redirects=True)
print r.url
print r.status_code
print r.history
