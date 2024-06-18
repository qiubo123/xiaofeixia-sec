#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Apache Flink 未授权访问',

      'level'     :   'low',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  target = '/config'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url,headers=headers,timeout=5,verify=False)
    version = re.findall(r'"flink-version":"(.*?)","', res.text)[0]
    list1 = version.split('.') #version格式为1.x.1 用split切割成数组
    if int(list1[1]) <= 10:#取中间为与10比较 小于等于10为true
      resp = get(url=url1,headers=headers,timeout=5,verify=False)
      if re.search(r'web-submit',resp.text,re.I):
        poc = re.findall(r'"web-submit":(.*?)}', resp.text)[0]
        if poc != 'false':
          # ret['huixian'] = res.text
          ret['ifbug'] = True
          res.close()
          return ret
        else:
          return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret