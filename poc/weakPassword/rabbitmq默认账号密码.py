#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'RabbitMQ默认账号密码',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      # 'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q='
      }
  target = '/api/whoami'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 401:
      pass
    else:
      return ret
    headers['Authorization'] = 'Basic Z3Vlc3Q6Z3Vlc3Q='
    resp=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'name.*?:.*?guest.*?tags.*?administrator',res.text,re.S):
    if resp.status_code == 200 and re.search(r'name.*?:.*?guest.*?tags.*?:',resp.text,re.S):
      resp.close()
      ret['huixian'] = 'rabbitmq默认账号/密码：guest/guest'
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret