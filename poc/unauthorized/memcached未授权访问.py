#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import script.getIP as getIP
import pymemcache.client.base as memcache_client
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Memcached未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/18',
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
  r0 = randomLowercase(4)
  r1 = randomLowercase(4)
  ret = msg()
  ip = getIP.main(url)
  if ip == None:
    return ret
  url1 = ip
  ret['url'] = f'{url1}:11211'

  try:
    client = memcache_client.Client((ip,11211))
    mset = client.set(r0,r1)
    # mget= client.get(r0)
    # print(mget)
    if mset == True:
      ret['huixian'] = f'{r0}:{r1}'
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret