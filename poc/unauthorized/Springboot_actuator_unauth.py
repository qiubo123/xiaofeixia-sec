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

      'bugname'   :   'springboot-actuator-unauth',

      'level'     :   'high',

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
  targets = ['/env','/actuator','/appenv','/api/actuator','/nacos/actuator','/prod-api/actuator','/dev-api/actuator']

  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  url4 = url + targets[3]
  url5 = url + targets[4]
  url6 = url + targets[5]
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url2
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url3
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url4,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url4
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url5,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url5
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    return ret
  try:
    res=requests.get(url=url6,headers=headers,timeout=5,verify=False)
    # if res.status_code == 200 and re.search(r'_links.*?self.*?health.*?env.*?heapdump',res.text,re.S):
    if res.status_code == 200 and re.search(r'java.version.*?os.arch',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret