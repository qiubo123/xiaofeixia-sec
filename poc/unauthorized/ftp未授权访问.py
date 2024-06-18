#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.getIP as getIP
import ftplib
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'FTP未授权访问',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/25',
  }
  return ret
def run(url,ua):
  # print(url)
  ret = msg()
  ip = getIP.main(url)
  url1 = ip
  ret['url'] = url
  if ip == None:
    return ret
  try:
    ftp = ftplib.FTP(ip)
    ftp.login()
    ftp.cwd('/')
    ftp.quit()
    ret['ifbug'] = True
    ret['huixian'] = url
    return ret
  except:
    return ret