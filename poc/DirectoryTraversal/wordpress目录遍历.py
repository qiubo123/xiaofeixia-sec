#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'WordPress 目录遍历',

      'level'     :   'low',

      'FOFA'      :   '',

      'ifbug'     :   False,

      'author'    :   'ppxfx',
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  try:
    res=requests.get(url=url+'/wp-admin/',headers=headers,timeout=5,verify=False)
    res2=requests.get(url=url+'/wp-content/',headers=headers,timeout=5,verify=False)
    res3=requests.get(url=url+'/wp-includes/',headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "Index of /" in res.text:
      res.close()
      ret['url'] = url+'/wp-admin/'
      ret['ifbug'] = True
      return ret
    if res2.status_code == 200 and "Index of /" in res2.text:
      res2.close()
      ret['url'] = url+'/wp-content/'
      ret['ifbug'] = True
      return ret
    if res3.status_code == 200 and "Index of /" in res3.text:
      res3.close()
      ret['url'] = url+'/wp-includes/'
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret