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

      'bugname'   :   'Elasticsearch未授权访问',

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
  url1 = f'http://{ip}:8000/_cat'
  ret['url'] = url1
  if ip == None:
    return ret
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if '/_cat/master' in res.text:
      ret['huixian'] = url
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret