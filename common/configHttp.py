import requests
import json
from common.Log import logger

logger = logger
class RunMain():

    def send_post(self, url, data,headers):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, data=data,headers=headers).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, data=data)
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None,headers=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data,headers)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
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
    headers = {'content-type': "application/json", 'Cookie': 'token=BearereyJhbGciOiJIUzUxMiJ9.eyJ1c2VySWRzIjoiZTlmNDQxYWQ1NmNlNGMzNTllMzRmMTljYjljZDM3ODAiLCJ0ZW5hbnRJZCI6IjAwMDAwMCIsInVzZXJOYW1lIjoiaHVqaWFuIiwiZXhwIjoxNTY1NjU5NzAyLCJ1c2VySWQiOiJlOWY0NDFhZDU2Y2U0YzM1OWUzNGYxOWNiOWNkMzc4MCJ9.zWPQxtYWR1YnahWr1x_hgRClPKMptRPakswdXeX0E8AzqvUzyVDuL8dXizZigtv1iOS6IFWHeIC8PU6cdQQFuw; Admin-Token=80f71640eba646c78022a183b2d72f08'}
    result = RunMain().run_main('post', 'http://10.0.95.8:8080/apis/msgc/crcMcSendtaskEx/task/query?',data=json.dumps(body),headers=headers)
    print(result)