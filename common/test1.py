import requests
import json
from common.Log import logger

'''def send_post(url, data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        print(result)
        #return res

if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    url = 'http://127.0.0.1:8888/login'
    d = 'name=yinxiong&pwd=123456'
    send_post(url=url,data=d)


from urllib.parse import parse_qs, urlparse

url = 'https://www.baidu.com/s?&wd=python&ie=utf-8'
# 提取url参数
query = urlparse(url).query
print(query)
# 将字符串转换为字典
param = parse_qs(query)
print(param)
"""所得的字典的value都是以列表的形式存在，若列表中都只有一个值"""
result = {key: param[key][0] for key in param}
result1 = {}
for key in param:
    print(key)
print(result)

from urllib.parse import parse_qs, urlparse
url = 'http://127.0.0.1:8888/login'
data = 'name=yinxiong&pwd=123456'
data1 = parse_qs(data)
req = requests.post(url,data1)
print(req.text)
print(type(req))'''

from urllib.parse import parse_qs, urlparse
url = 'http://10.0.95.8:8080/apis/msgc/crcMcSendtaskEx/task/query'
body = {
  "pageNum": 1,
  "pageSize": 10,
  "list": [
    {
      "taskGuid": "",
      "taskStatus": "",
      "sendStartTime": "",
      "sendEndTime": ""
    }
  ]
}
print(type(body))
print(type(json.dumps(body)))
headers = {'content-type': "application/json", 'Cookie': 'token=BearereyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWRzIjoiZTlmNDQxYWQ1NmNlNGMzNTllMzRmMTljYjljZDM3ODAiLCJ0ZW5hbnRJZCI6IjAwMDAwMCIsInVzZXJOYW1lIjoiaHVqaWFuIiwiZXhwIjoxNTY1NjU5NzAyLCJ1c2VySWQiOiJlOWY0NDFhZDU2Y2U0YzM1OWUzNGYxOWNiOWNkMzc4MCJ9.zWPQxtYWR1YnahWr1x_hgRClPKMptRPakswdXeX0E8AzqvUzyVDuL8dXizZigtv1iOS6IFWHeIC8PU6cdQQFuw; Admin-Token=80f71640eba646c78022a183b2d72f08'}
print(type(headers))
#data1 = parse_qs(data)
req = requests.post(url,data = json.dumps(body),headers = headers)
ss = json.loads(str(req.text))
print(req.text)
print (req.status_code)
print(ss['code'])

'''a = "{1: 'a', 2: 'b'}"
# 将字符串转化为字典
# 1.通过eval()方法转化，但缺乏安全性
b = eval(a)
print(type(b))

# 2.通过json 来转换,但是使用 json 进行转换存在一个潜在的问题，由于 json 语法规定 数组或对象之中的字符串必须使用双引号，不能使用单引号
#以下运行会报错
a = "{'a':1,'b':2}"
b = json.loads(a)
print(type(b))

#将字典转化为字符串
a = {'a':1,'b':2}
#b = str(a)
b = json.dumps(a)
print(type(b)'''