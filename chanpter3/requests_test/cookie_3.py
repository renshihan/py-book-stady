#coding:utf-8
import requests
# 自定义cookie值发送出去，可以使用以下方法，示例如下：
loginUrl='http://localhost:8080/test/pythonT'
s=requests.session()

# 首先访问登录页面，作为游客，服务器会优先分配一个cookie
r=s.get(loginUrl,allow_redirects=True)
datas={'username':'renshihan','password':'1234'}
# 向登录链接发送post请求，验证成功，游客权限转为会员权限
r=s.post(loginUrl,data=datas,allow_redirects=True)
print r.text




#  