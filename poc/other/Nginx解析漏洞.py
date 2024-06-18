#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Nginx 解析漏洞',

      'level'     :   'medium',

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
    vurl1 = url + '/.php'
    vurl2 = url + '/.xxx'
    vurl3 = url + '/.a'
    rep1 = requests.get(vurl1, headers=headers)
    rep2 = requests.get(vurl2, headers=headers)
    rep3 = requests.get(vurl3, headers=headers)
    if 'nginx' in str(res.headers):
      res.close()
      if len(rep1.text) != len(rep2.text) and len(rep1.text) != len(rep3.text) and len(rep2.text) == len(rep3.text):
        ret['ifbug'] = True
        rep1.close()
        rep2.close()
        rep3.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret