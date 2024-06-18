#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.getIP as getIP
import redis
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Redis未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/20',
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
  r0 = randomLowercase(5)
  r1 = randomLowercase(5)
  ret = msg()
  ip = getIP.main(url)
  ret['url'] = ip
  if ip == None:
    return ret
  try:
    r = r = redis.StrictRedis(host=ip,port=6379)
    rset = r.set(r0,r1)
    if rset == True:
      ret['url'] = f'{ip}:6379'
      ret['huixian'] = f'{r0}:{r1}'
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret