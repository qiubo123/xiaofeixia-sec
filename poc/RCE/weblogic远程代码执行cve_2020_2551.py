#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '特征检测，可能是误报，请手工检查',

      'method'    :   'get',

      'bugname'   :   'WebLogic 远程代码执行 CVE-2020-2551',

      'level'     :   'critical',

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
  targets = [
      '/console/login/LoginForm.jsp',
      ':7001/console/login/LoginForm.jsp'
      ]
  url1 = url + targets[0]
  url2 = url + targets[1]
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "WebLogic" in res.text:
      if '10.3.6.0' in res.text or '12.1.3.0' in res.text or '12.2.1.3' in res.text or '12.2.1.4' in res.text:
        res.close()
        ret['ifbug'] = True
        return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "WebLogic" in res.text:
      if '10.3.6.0' in res.text or '12.1.3.0' in res.text or '12.2.1.3' in res.text or '12.2.1.4' in res.text:
        ret['url'] = url2
        res.close()
        ret['ifbug'] = True
        return ret
  except:
    pass
  return ret