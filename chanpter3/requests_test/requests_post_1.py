#coding:utf-8
# requests是第三方模块，需要额外完成安装
import requests

def post(url,postdata):
    r=requests.post(url,data=postdata)
    return r.content

def get(url):
    r = requests.get(url)
    return r.content

# put
def put(url,postdata):
    r = requests.put(url, data=postdata)
    return r.content

def delete(url,postdata):
    r = requests.delete(url, data=postdata)
    return r.content

def head(url,postdata):
    r = requests.head(url, data=postdata)
    return r.content

def options(url,postdata):
    r = requests.options(url, data=postdata)
    return r.content


def http(url,data):
    if data:
        return post(url,data)
    return get(url)

if __name__ == '__main__':
    postdata = {'username': 'renshihan', 'password': '123456'}
    url = 'http://localhost:8080/test/pythonT'
    print http(url,postdata)

