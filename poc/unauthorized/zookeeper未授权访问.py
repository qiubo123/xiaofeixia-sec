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

      'bugname'   :   'ZooKeeper未授权访问',

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
  url1 = f'vnc://{ip}'
  ret['url'] = url1
  if ip == None:
    return ret
  try:
    tigerVNC_response = requests.get(url=url1,timeout=5)
    if "RFB 003.008\n" in tigerVNC_response.content.decode('utf-8'):
      ret['ifbug'] = True
      ret['huixian'] = url
      return ret
    else:
      return ret
  except:
    return ret