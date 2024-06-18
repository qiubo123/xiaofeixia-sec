#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "Druid未授权访问漏洞"
  ret['level'] = "medium"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/druid/index.html","/fdfsdruid/index.html","/prod-api/druid/index.html"]
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "Druid Stat Index" in res.text:
      ret['ifbug'] = True
      ret['url'] = url1
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "Druid Stat Index" in res.text:
      ret['ifbug'] = True
      ret['url'] = url2
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and "Druid Stat Index" in resp.text:
      ret['ifbug'] = True
      resp.close()
      ret['url'] = url3
      return ret
    else:
      return ret
  except:
    return ret