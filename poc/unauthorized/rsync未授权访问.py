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

      'bugname'   :   'Rsync未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  ip = getIP.main(url)
  if ip == None:
    return ret
  headers = {
      'User-Agent': ua,
      }
  url1 = f'rsync://{ip}'
  ret['url'] = url1
  try:
    res=requests.get(url=url1,timeout=5)
    if 'rsync' in res.headers.get('Server','') and 'rsyncd.conf' in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret