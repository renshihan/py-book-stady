#coding:utf-8

import httplib

cone=None
try:
    conn=httplib.HTTPConnection("127.0.0.1:8080")        #创建HTTPConnection对象        www.zhihu.com
    conn.request("GET","/test/index") #发送请求
    response=conn.getresponse()         #获取响应
    print response.status,response.reason

    print '_' * 40

    headers=response.getheaders()
    for h in headers:
        print h

    print '_'*40
    print response.msg

except Exception,e:
    print e
finally:
    if conn:
        conn.close()
