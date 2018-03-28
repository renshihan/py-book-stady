import httplib,urllib

conn=None
try:
    params=urllib.urlencode({'name':'mr.renshihan','age':22})
    headers={'Content-type':'application/x-www-form-unlencoded',"Accept":"text/plain"}
    conn=httplib.HTTPConnection("www.zhihu.com",80,timeout=3)
    conn.request('POST','/login',params,headers)
    response=conn.getresponse()
    print '_' * 40

    for header in response.getheaders():
        print header
    print '_' * 40

    print response.status
    print response.read()
except Exception,e:
    print e
finally:
    if conn:
        conn.close()