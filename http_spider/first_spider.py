# @author :xpzhuang
# @date : 2020/11/1

import urllib3

http=urllib3.PoolManager()
response=http.request('GET','https://www.baidu.com/')
print(response.data)

response=http.request('POST','http://httpbin.org/post',fields={'word':'hello'})
print(response.data)