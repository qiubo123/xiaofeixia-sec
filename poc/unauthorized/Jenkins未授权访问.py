#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.getIP as getIP
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Jenkins未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/16',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  ip = getIP.main(url)
  if ip == None:
    return ret
  url1 = f'http://{ip}:8080'
  url1 = url1
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if 'jenkins' in response.headers.get('X-Jenkins', '') and 'Dashboard [Jenkins]' in res.text:
      ret['huixian'] = url
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret