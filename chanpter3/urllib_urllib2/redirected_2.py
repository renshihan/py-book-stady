#coding:utf-8
# 不想自动重定向，可以自定义HTTPRedircectHandle

import urllib2


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self,req,fp,code,msg,headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result=urllib2.HTTPRedirectHandler.http_error_301(self,req,fp,code,msg,headers)
        result.status=code
        result.newurl=result.geturl()
        return result

opener=urllib2.build_opener(RedirectHandler)
opener.open('http://www.zhihu.com')