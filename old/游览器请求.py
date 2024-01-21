'''requests
作用：使用requests可以模拟浏览器请求，比起之前用的urllib，requests模块的api更加便捷
安装：pip install requests
请求方式：
requests.get()
requests.post()
requests.put()
requests.delete()
requests.head()
requests.options()

'''

import requests
#基于requests之GET请求
#1.基本请求（text可能会返回乱码）
res = requests.get('https://www.baidu.com')
print(res.content.decode('utf8')) #content二进制格式，decode()字节串转成字符串
print(res.text) #text字符串格式


