import requests
import chardet

# 直接将chardet探测到的编码，赋给r.encoding实现解码，r.text输出就不会有乱码了。

r=requests.get("http://www.baidu.com")
print chardet.detect(r.content)

r.encoding=chardet.detect(r.content)['encoding']

print r.text