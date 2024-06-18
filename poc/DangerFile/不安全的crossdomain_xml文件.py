#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "不安全的crossdomain漏洞"
  ret['level'] = "high"
  ret['ifbug'] = False
  ret['author'] = 'ppxfx'
  ret['FOFA'] = ''
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target="/crossdomain.xml"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=6,verify=False)
    if 'allow-access-from domain="*"' in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
