#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)
def msg():
  ret = {}
  ret['links'] = []
  ret['huixian'] = []
  ret['method'] = 'get'
  ret['bugname'] = "Apache Active MQ未授权访问漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  payload= "/admin"#8161
  url1 = url + payload
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "ActiveMQ Console of" in res.text or res.status_code == 200 and 'Apache ActiveMQ' in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret