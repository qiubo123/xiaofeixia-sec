#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "SwaggerUI未授权访问漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/swagger-ui.html",'/swagger/index.html','/swagger/ui/index','/swagger-ui/index.html']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  url4 = url + targets[3]
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if 'Swagger' in res.text:
      res.close()
      ret['ifbug'] = True
      ret['url'] = url1
      return ret
  except:
    pass
  try:
    res2=requests.get(url=url2,headers=headers,timeout=10,verify=False)
    if 'Swagger' in res2.text:
      res2.close()
      ret['ifbug'] = True
      ret['url'] = url2
      return ret
  except:
    pass
  try:
    res3=requests.get(url=url3,headers=headers,timeout=10,verify=False)
    if 'Swagger' in res3.text:
      res3.close()
      ret['ifbug'] = True
      ret['url'] = url3
      return ret
  except:
    pass
  try:
    # print(url4)
    res4=requests.get(url=url4,headers=headers,timeout=10,verify=False)
    # print(res4.text)
    if 'Swagger' in res4.text:
      res3.close()
      ret['ifbug'] = True
      ret['url'] = url4
      return ret
    else:
      return ret
  except:
    return ret