#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://blog.csdn.net/qq_44159028/article/details/114659086',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'vSphere Client CVE-2021-21972',

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
      "Content-Type":"application/x-www-form-urlencoded"
      }
  target = '/sdk/vimServiceVersions.xml'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search("<version>.+</version>", res.text):
      res.close()
      rep = requests.get(url+'/ui/vropspluginui/rest/services/uploadova', headers=headers, timeout=timeout, verify=False)
      if rep.status_code == 405 and 'Method Not Allowed' in rep.text:
        # ret['huixian'] = res.text
        rep.close()
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret