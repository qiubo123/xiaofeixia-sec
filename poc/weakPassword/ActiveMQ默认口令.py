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

      'bugname'   :   'ActiveMQ Default Password',

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
  headers = {
      'User-Agent': ua,
      }
  target = '/admin/'
  url1 = url + target
  ret['url'] = url1
  admin = base64Str('admin:admin')
  user = base64Str('user:user')
  try:
    headers['Authorization'] = f'Basic {admin}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code ==200 and 'Welcome to the Apache ActiveMQ Console of' in res.text and '<h2>Broker</h2>' in res.text:
      ret['huixian'] = "账号/密码：admin/admin"
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    headers['Authorization'] = f'Basic {user}'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code ==200 and 'Welcome to the Apache ActiveMQ Console of' in res.text and '<h2>Broker</h2>' in res.text:
      ret['huixian'] = "账号/密码：user/user"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret